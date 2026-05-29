from __future__ import annotations

from pathlib import Path

from dental_packet.deidentify import redact_text


def read_optional_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        return redact_text(path.read_text(encoding="utf-8")).strip()
    except UnicodeDecodeError:
        return ""


def summarize_text(text: str, max_chars: int = 1200) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= max_chars:
        return cleaned
    return f"{cleaned[: max_chars - 3].rstrip()}..."


def build_case_overview(chief_complaint: str, clinical_notes: str, treatment_plan: str) -> str:
    parts = []
    if chief_complaint:
        parts.append(f"Chief complaint: {summarize_text(chief_complaint, 300)}")
    if clinical_notes:
        parts.append(f"Clinical notes available: {summarize_text(clinical_notes, 500)}")
    if treatment_plan:
        parts.append(f"Treatment plan available: {summarize_text(treatment_plan, 500)}")
    if not parts:
        return "No narrative dental records were provided."
    return " ".join(parts)

