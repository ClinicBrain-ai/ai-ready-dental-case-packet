from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from dental_packet.cli import build as build_pipeline
from dental_packet.schemas import CasePacket
from dental_packet.validator import validate_case_packet as validate_packet_file

SAFETY_DISCLAIMER = (
    "For clinical review only. This MCP server does not diagnose, does not recommend "
    "treatment, does not claim clinical accuracy, and does not send patient data to external APIs."
)

PHI_FIELD_HINTS = {
    "address",
    "birthdate",
    "birth_date",
    "date_of_birth",
    "dob",
    "email",
    "institution",
    "institutionaddress",
    "institutionname",
    "name",
    "patientaddress",
    "patientbirthdate",
    "patientid",
    "patientname",
    "phone",
    "telephone",
}

PHI_VALUE_PATTERNS = {
    "email-like text": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone-like text": re.compile(r"\b(?:\+?\d[\d .()/-]{7,}\d)\b"),
    "date-like text": re.compile(r"\b(?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2}\b"),
}


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_warnings(output_folder: Path) -> list[str]:
    log_path = output_folder / "logs" / "pipeline.log"
    if not log_path.exists():
        return []
    return [line for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _safe_path(path: Path) -> str:
    return path.expanduser().resolve().as_posix()


def build_dental_case_packet(input_folder: str, output_folder: str) -> dict[str, Any]:
    """Run the local Dental Case Packet build pipeline."""
    output_path = Path(output_folder).expanduser()
    try:
        build_pipeline(input=Path(input_folder).expanduser(), output=output_path)
        return {
            "success": True,
            "case_packet_path": _safe_path(output_path / "case_packet.json"),
            "markdown_report_path": _safe_path(output_path / "case_packet.md"),
            "manifest_path": _safe_path(output_path / "manifest.json"),
            "warnings": _read_warnings(output_path),
        }
    except Exception as exc:
        return {
            "success": False,
            "case_packet_path": _safe_path(output_path / "case_packet.json"),
            "markdown_report_path": _safe_path(output_path / "case_packet.md"),
            "manifest_path": _safe_path(output_path / "manifest.json"),
            "warnings": [f"{type(exc).__name__}: {exc}"],
        }


def validate_case_packet(case_packet_path: str) -> dict[str, Any]:
    """Validate a Dental Case Packet JSON file without sending data anywhere."""
    try:
        validate_packet_file(Path(case_packet_path).expanduser())
    except ValidationError as exc:
        return {
            "valid": False,
            "errors": [
                {
                    "field": ".".join(str(part) for part in error["loc"]),
                    "message": error["msg"],
                }
                for error in exc.errors()
            ],
            "warnings": [],
        }
    except Exception as exc:
        return {
            "valid": False,
            "errors": [{"field": "case_packet_path", "message": f"{type(exc).__name__}: {exc}"}],
            "warnings": [],
        }
    return {"valid": True, "errors": [], "warnings": []}


def summarize_packet(case_packet_path: str) -> dict[str, Any]:
    """Return a non-diagnostic, dentist-review-only summary."""
    packet = CasePacket.model_validate(_read_json(Path(case_packet_path).expanduser()))
    imaging = packet.imaging
    available_records = []
    if packet.chief_complaint:
        available_records.append("chief_complaint")
    if packet.clinical_notes_summary:
        available_records.append("clinical_notes")
    if packet.treatment_plan_summary:
        available_records.append("treatment_plan")
    if imaging.cbct.available:
        available_records.append("cbct")
    if imaging.xray.available:
        available_records.append("xray")
    if imaging.intraoral_scan.available:
        available_records.append("intraoral_scan")
    if imaging.photos.available:
        available_records.append("photos")

    return {
        "case_overview": packet.ai_ready_context.case_overview,
        "available_records": available_records,
        "missing_information": packet.ai_ready_context.missing_information,
        "dentist_review_questions": packet.ai_ready_context.clinical_review_questions,
        "safety_disclaimer": SAFETY_DISCLAIMER,
    }


def list_supported_formats() -> dict[str, list[str]]:
    """List supported input formats for structured data transformation."""
    return {
        "CBCT/DICOM": [".dcm"],
        "X-ray DICOM/JPG/PNG": [".dcm", ".jpg", ".jpeg", ".png"],
        "intraoral scan STL/PLY/OBJ": [".stl", ".ply", ".obj"],
        "photos JPG/PNG": [".jpg", ".jpeg", ".png"],
        "text notes TXT": [".txt"],
    }


def _walk_json(value: Any, path: str = "$") -> list[tuple[str, Any]]:
    items = [(path, value)]
    if isinstance(value, dict):
        for key, child in value.items():
            items.extend(_walk_json(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            items.extend(_walk_json(child, f"{path}[{index}]"))
    return items


def check_phi_risk(case_packet_path: str) -> dict[str, Any]:
    """Check for obvious PHI-like fields without returning actual PHI values."""
    data = _read_json(Path(case_packet_path).expanduser())
    flagged_fields: set[str] = set()

    for path, value in _walk_json(data):
        field_name = path.rsplit(".", maxsplit=1)[-1].lower().replace("_", "")
        if field_name in PHI_FIELD_HINTS:
            flagged_fields.add(path)
        if isinstance(value, str):
            for label, pattern in PHI_VALUE_PATTERNS.items():
                if pattern.search(value):
                    flagged_fields.add(f"{path} ({label})")

    if not flagged_fields:
        risk_level = "low"
        recommendations = [
            "No obvious PHI-like fields were detected in the packet.",
            "Review generated packets before sharing outside approved clinical workflows.",
        ]
    else:
        risk_level = "medium" if len(flagged_fields) <= 3 else "high"
        recommendations = [
            "Review flagged field paths before sharing the packet.",
            "Do not paste raw patient identifiers into AI tools.",
            "Regenerate the packet after removing source PHI if flagged fields are unexpected.",
        ]

    return {
        "risk_level": risk_level,
        "flagged_fields": sorted(flagged_fields),
        "recommendations": recommendations,
    }
