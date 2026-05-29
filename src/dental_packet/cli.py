from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated, Any

import typer

from dental_packet.deidentify import create_deidentified_copies, read_patient_info
from dental_packet.dicom_parser import scan_dicom_dir
from dental_packet.file_indexer import build_file_index
from dental_packet.report_writer import write_markdown_report
from dental_packet.scan_parser import parse_intraoral_scans
from dental_packet.schemas import AiReadyContext, CasePacket, Imaging, Manifest, Patient
from dental_packet.text_processor import build_case_overview, read_optional_text, summarize_text
from dental_packet.validator import validate_case_packet

app = typer.Typer(help="Build de-identified AI-ready dental case packets.")


def _write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str), encoding="utf-8")


def _image_records(input_root: Path, role: str, extensions: set[str]) -> list[dict[str, Any]]:
    root = input_root / role
    if not root.exists():
        return []
    return [
        {"path": path.relative_to(input_root).as_posix(), "format": path.suffix.lower().lstrip(".")}
        for path in sorted(
            p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in extensions
        )
    ]


def _missing_information(packet_inputs: dict[str, bool]) -> list[str]:
    labels = {
        "chief_complaint": "chief_complaint.txt",
        "clinical_notes": "clinical_notes.txt",
        "treatment_plan": "treatment_plan.txt",
        "cbct": "CBCT DICOM records",
        "xray": "X-ray records",
        "intraoral_scan": "Intraoral scan files",
        "photos": "Clinical photos",
    }
    return [f"Missing {label}." for key, label in labels.items() if not packet_inputs[key]]


def _review_questions(missing: list[str]) -> list[str]:
    questions = [
        "Please confirm that the de-identified packet accurately reflects the available records.",
        (
            "Please identify whether any omitted source records should be added before AI "
            "workflow use."
        ),
    ]
    if missing:
        questions.append(
            "Please confirm whether the missing records are unavailable or intentionally omitted."
        )
    return questions


def _llm_prompt_context(case_overview: str, missing: list[str]) -> str:
    missing_text = "; ".join(missing) if missing else "No obvious missing record categories."
    return (
        "You are reviewing a de-identified dental case packet. Do not diagnose. Do not provide "
        "treatment recommendations. Summarize the available information, identify missing records, "
        "and generate questions for dentist review. All output is for clinical review only.\n\n"
        f"Case overview: {case_overview}\nMissing information: {missing_text}"
    )


@app.command()
def build(
    input: Annotated[Path, typer.Option("--input", "-i", help="Input folder.")],
    output: Annotated[Path, typer.Option("--output", "-o", help="Output folder.")],
) -> None:
    """Build a de-identified structured dental case packet."""
    output.mkdir(parents=True, exist_ok=True)
    for dirname in ["deidentified", "thumbnails", "logs"]:
        (output / dirname).mkdir(exist_ok=True)

    logs: list[str] = []
    now = datetime.now(UTC)
    manifest_items = build_file_index(input)
    manifest = Manifest(created_at=now, input_root=str(input), files=manifest_items)
    _write_json(output / "manifest.json", manifest.model_dump(mode="json"))
    _write_json(output / "files_index.json", [item.model_dump() for item in manifest_items])

    logs.extend(create_deidentified_copies(input, output))

    patient_info = read_patient_info(input / "patient_info.json")
    chief_complaint = read_optional_text(input / "chief_complaint.txt")
    clinical_notes = read_optional_text(input / "clinical_notes.txt")
    treatment_plan = read_optional_text(input / "treatment_plan.txt")

    cbct_summary, _, cbct_warnings = scan_dicom_dir(input / "cbct", "cbct")
    xray_dicom_summary, xray_dicom_files, xray_warnings = scan_dicom_dir(input / "xray", "xray")
    logs.extend(cbct_warnings)
    logs.extend(xray_warnings)

    xray_image_files = _image_records(input, "xray", {".jpg", ".jpeg", ".png"})
    photo_files = _image_records(input, "photos", {".jpg", ".jpeg", ".png"})
    scan_files, scan_formats, scan_warnings = parse_intraoral_scans(input)
    logs.extend(scan_warnings)

    case_overview = build_case_overview(chief_complaint, clinical_notes, treatment_plan)
    packet_inputs = {
        "chief_complaint": bool(chief_complaint),
        "clinical_notes": bool(clinical_notes),
        "treatment_plan": bool(treatment_plan),
        "cbct": bool(cbct_summary["available"]),
        "xray": bool(xray_dicom_files or xray_image_files),
        "intraoral_scan": bool(scan_files),
        "photos": bool(photo_files),
    }
    missing = _missing_information(packet_inputs)
    known = [key for key, available in packet_inputs.items() if available]
    questions = _review_questions(missing)

    imaging = Imaging.model_validate(
        {
            "cbct": {
                **cbct_summary,
                "warnings": cbct_warnings,
            },
            "xray": {
                "available": bool(xray_dicom_files or xray_image_files),
                "files": xray_dicom_files + xray_image_files,
                "dicom_metadata_summary": xray_dicom_summary["dicom_metadata_summary"],
                "warnings": xray_warnings,
            },
            "intraoral_scan": {
                "available": bool(scan_files),
                "files": scan_files,
                "formats": scan_formats,
            },
            "photos": {
                "available": bool(photo_files),
                "files": photo_files,
            },
        }
    )

    packet = CasePacket(
        case_id=f"case-{uuid.uuid4().hex[:12]}",
        created_at=now,
        patient=Patient(
            age=patient_info.get("age"),
            sex=patient_info.get("sex"),
            deidentified=True,
        ),
        chief_complaint=summarize_text(chief_complaint),
        clinical_notes_summary=summarize_text(clinical_notes),
        treatment_plan_summary=summarize_text(treatment_plan),
        imaging=imaging,
        ai_ready_context=AiReadyContext(
            case_overview=case_overview,
            known_information=known,
            missing_information=missing,
            clinical_review_questions=questions,
            llm_prompt_context=_llm_prompt_context(case_overview, missing),
        ),
    )

    _write_json(output / "case_packet.json", packet.model_dump(mode="json"))
    write_markdown_report(packet, output / "case_packet.md")
    (output / "logs" / "pipeline.log").write_text(
        "\n".join(logs) + ("\n" if logs else ""),
        encoding="utf-8",
    )
    typer.echo(f"Built case packet: {output / 'case_packet.json'}")


@app.command()
def validate(
    input: Annotated[Path, typer.Option("--input", "-i", help="Path to case_packet.json.")],
) -> None:
    """Validate a generated case packet JSON file."""
    validate_case_packet(input)
    typer.echo("case_packet.json is valid")


if __name__ == "__main__":
    app()
