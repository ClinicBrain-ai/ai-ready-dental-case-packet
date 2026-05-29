from __future__ import annotations

import json

from typer.testing import CliRunner

from dental_packet.cli import app

runner = CliRunner()


def test_build_empty_folder(tmp_path) -> None:
    input_root = tmp_path / "project-input"
    output_root = tmp_path / "case_packet_output"
    input_root.mkdir()

    result = runner.invoke(app, ["build", "--input", str(input_root), "--output", str(output_root)])

    assert result.exit_code == 0, result.output
    packet = json.loads((output_root / "case_packet.json").read_text(encoding="utf-8"))
    assert packet["patient"]["deidentified"] is True
    assert packet["safety"]["not_for_diagnosis"] is True
    assert packet["imaging"]["cbct"]["available"] is False


def test_build_only_treatment_plan_and_validate(tmp_path) -> None:
    input_root = tmp_path / "project-input"
    output_root = tmp_path / "case_packet_output"
    input_root.mkdir()
    (input_root / "treatment_plan.txt").write_text(
        "Patient email patient@example.com. Existing dentist treatment plan text.",
        encoding="utf-8",
    )

    build_result = runner.invoke(
        app,
        ["build", "--input", str(input_root), "--output", str(output_root)],
    )
    assert build_result.exit_code == 0, build_result.output

    packet_path = output_root / "case_packet.json"
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    assert "patient@example.com" not in packet["treatment_plan_summary"]
    assert "for clinical review only" in packet["ai_ready_context"]["llm_prompt_context"].lower()

    validate_result = runner.invoke(app, ["validate", "--input", str(packet_path)])
    assert validate_result.exit_code == 0, validate_result.output
