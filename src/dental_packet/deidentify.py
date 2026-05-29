from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any

PATIENT_INFO_ALLOWLIST = {"age", "sex"}

EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
PHONE_RE = re.compile(r"(?<!\d)(?:\+?\d[\d .()-]{7,}\d)(?!\d)")
DATE_RE = re.compile(r"\b(?:19|20)\d{2}[-/年](?:0?[1-9]|1[0-2])[-/月](?:0?[1-9]|[12]\d|3[01])日?\b")


def redact_text(text: str) -> str:
    redacted = EMAIL_RE.sub("[REDACTED_EMAIL]", text)
    redacted = PHONE_RE.sub("[REDACTED_PHONE]", redacted)
    return DATE_RE.sub("[REDACTED_DATE]", redacted)


def deidentify_patient_info(data: dict[str, Any]) -> dict[str, Any]:
    return {key: data.get(key) for key in PATIENT_INFO_ALLOWLIST if key in data}


def read_patient_info(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}
    if not isinstance(raw, dict):
        return {}
    return deidentify_patient_info(raw)


def create_deidentified_copies(input_root: Path, output_root: Path) -> list[str]:
    deidentified_root = output_root / "deidentified"
    deidentified_root.mkdir(parents=True, exist_ok=True)
    warnings: list[str] = []

    if not input_root.exists():
        return warnings

    for path in sorted(p for p in input_root.rglob("*") if p.is_file()):
        relative = path.relative_to(input_root)
        target = deidentified_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)

        if path.suffix.lower() == ".txt":
            try:
                target.write_text(redact_text(path.read_text(encoding="utf-8")), encoding="utf-8")
            except UnicodeDecodeError:
                warnings.append(f"Could not decode text file for de-identification: {relative}")
        elif relative.as_posix() == "patient_info.json":
            info = read_patient_info(path)
            target.write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
        elif path.suffix.lower() == ".dcm":
            warnings.append(
                f"DICOM copied by reference only; metadata PHI is not exported: {relative}"
            )
        else:
            shutil.copy2(path, target)

    return warnings
