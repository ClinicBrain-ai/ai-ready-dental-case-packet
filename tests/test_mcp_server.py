from __future__ import annotations

import json
import sys

from dental_packet_mcp.core import (
    build_dental_case_packet,
    check_phi_risk,
    list_supported_formats,
    summarize_packet,
    validate_case_packet,
)
from dental_packet_mcp.server import main


def test_mcp_build_validate_and_summarize(tmp_path) -> None:
    input_root = tmp_path / "project-input"
    output_root = tmp_path / "case_packet_output"
    input_root.mkdir()
    (input_root / "chief_complaint.txt").write_text("Patient reports tooth discomfort.", "utf-8")
    (input_root / "treatment_plan.txt").write_text("Existing dentist plan text.", "utf-8")

    build_result = build_dental_case_packet(
        input_folder=str(input_root),
        output_folder=str(output_root),
    )

    assert build_result["success"] is True
    assert build_result["case_packet_path"].endswith("case_packet.json")
    assert build_result["markdown_report_path"].endswith("case_packet.md")
    assert build_result["manifest_path"].endswith("manifest.json")

    validate_result = validate_case_packet(build_result["case_packet_path"])
    assert validate_result == {"valid": True, "errors": [], "warnings": []}

    summary = summarize_packet(build_result["case_packet_path"])
    assert "diagnose" in summary["safety_disclaimer"]
    assert "treatment" in summary["safety_disclaimer"]
    assert "chief_complaint" in summary["available_records"]
    assert "dentist_review_questions" in summary


def test_mcp_supported_formats() -> None:
    formats = list_supported_formats()

    assert ".dcm" in formats["CBCT/DICOM"]
    assert ".stl" in formats["intraoral scan STL/PLY/OBJ"]
    assert ".txt" in formats["text notes TXT"]


def test_mcp_help_does_not_start_server(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["dental-packet-mcp", "--help"])

    main()

    output = capsys.readouterr().out
    assert "Dental Case Packet MCP" in output
    assert "build_dental_case_packet" in output
    assert "No diagnosis" in output


def test_mcp_phi_risk_flags_paths_not_values(tmp_path) -> None:
    packet_path = tmp_path / "case_packet.json"
    packet_path.write_text(
        json.dumps(
            {
                "case_id": "case-test",
                "created_at": "2026-05-29T00:00:00Z",
                "patient": {"age": None, "sex": None, "deidentified": True},
                "chief_complaint": "Contact patient@example.com",
                "clinical_notes_summary": "",
                "treatment_plan_summary": "",
                "imaging": {
                    "cbct": {
                        "available": False,
                        "series_count": 0,
                        "dicom_metadata_summary": {},
                        "warnings": [],
                    },
                    "xray": {"available": False, "files": []},
                    "intraoral_scan": {"available": False, "files": [], "formats": []},
                    "photos": {"available": False, "files": []},
                },
                "ai_ready_context": {
                    "case_overview": "",
                    "known_information": [],
                    "missing_information": [],
                    "clinical_review_questions": [],
                    "llm_prompt_context": "",
                },
                "safety": {
                    "not_for_diagnosis": True,
                    "requires_dentist_review": True,
                    "phi_removed": True,
                },
            }
        ),
        encoding="utf-8",
    )

    result = check_phi_risk(str(packet_path))

    assert result["risk_level"] == "medium"
    assert "$.chief_complaint (email-like text)" in result["flagged_fields"]
    assert "patient@example.com" not in json.dumps(result)


def test_mcp_phi_risk_ignores_packet_created_at(tmp_path) -> None:
    packet_path = tmp_path / "case_packet.json"
    packet_path.write_text(
        json.dumps(
            {
                "case_id": "case-test",
                "created_at": "2026-05-29T00:00:00Z",
                "patient": {"age": None, "sex": None, "deidentified": True},
                "chief_complaint": "",
                "clinical_notes_summary": "",
                "treatment_plan_summary": "",
                "imaging": {
                    "cbct": {
                        "available": False,
                        "series_count": 0,
                        "dicom_metadata_summary": {},
                        "warnings": [],
                    },
                    "xray": {"available": False, "files": []},
                    "intraoral_scan": {"available": False, "files": [], "formats": []},
                    "photos": {"available": False, "files": []},
                },
                "ai_ready_context": {
                    "case_overview": "",
                    "known_information": [],
                    "missing_information": [],
                    "clinical_review_questions": [],
                    "llm_prompt_context": "",
                },
                "safety": {
                    "not_for_diagnosis": True,
                    "requires_dentist_review": True,
                    "phi_removed": True,
                },
            }
        ),
        encoding="utf-8",
    )

    assert check_phi_risk(str(packet_path))["risk_level"] == "low"
