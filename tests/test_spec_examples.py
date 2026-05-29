from __future__ import annotations

from pathlib import Path

from dental_packet.validator import validate_case_packet


def test_spec_examples_validate() -> None:
    examples_root = Path("examples/case_packets")

    for path in sorted(examples_root.glob("*.json")):
        packet = validate_case_packet(path)
        assert packet.patient.deidentified is True
        assert packet.safety.not_for_diagnosis is True
        assert packet.safety.requires_dentist_review is True
        assert packet.safety.phi_removed is True
        assert "do not diagnose" in packet.ai_ready_context.llm_prompt_context.lower()

