from __future__ import annotations

from datetime import UTC, datetime

from dental_packet.schemas import CasePacket


def test_case_packet_schema_valid() -> None:
    packet = CasePacket(case_id="case-test", created_at=datetime.now(UTC))
    assert packet.patient.deidentified is True
    assert packet.safety.not_for_diagnosis is True
    assert packet.safety.requires_dentist_review is True

