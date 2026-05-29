from __future__ import annotations

from pathlib import Path

from dental_packet.schemas import CasePacket

DISCLAIMER = (
    "This packet is for clinical review only. It is not for diagnosis and does not provide "
    "treatment recommendations. A licensed dentist must review all source records."
)


def write_markdown_report(packet: CasePacket, path: Path) -> None:
    lines = [
        f"# Dental Case Packet: {packet.case_id}",
        "",
        "> For clinical review only. Not for diagnosis. Requires dentist review.",
        "",
        "## Case Overview",
        packet.ai_ready_context.case_overview or "No overview available.",
        "",
        "## Available Records",
        f"- Chief complaint: {'available' if packet.chief_complaint else 'missing'}",
        f"- Clinical notes: {'available' if packet.clinical_notes_summary else 'missing'}",
        f"- Treatment plan: {'available' if packet.treatment_plan_summary else 'missing'}",
        "",
        "## Imaging Inventory",
        f"- CBCT DICOM: {'available' if packet.imaging.cbct.available else 'missing'}",
        f"- X-ray files: {len(packet.imaging.xray.files)}",
        f"- Intraoral scans: {len(packet.imaging.intraoral_scan.files)}",
        f"- Photos: {len(packet.imaging.photos.files)}",
        "",
        "## Treatment Plan Summary",
        packet.treatment_plan_summary or "No treatment plan was provided.",
        "",
        "## Missing Information",
    ]
    lines.extend(f"- {item}" for item in packet.ai_ready_context.missing_information)
    lines.extend(
        [
            "",
            "## Questions for Dentist Review",
        ]
    )
    lines.extend(f"- {item}" for item in packet.ai_ready_context.clinical_review_questions)
    lines.extend(["", "## AI Use Disclaimer", DISCLAIMER, ""])
    path.write_text("\n".join(lines), encoding="utf-8")

