from __future__ import annotations

import json
from pathlib import Path

from dental_packet.schemas import CasePacket


def validate_case_packet(path: Path) -> CasePacket:
    return CasePacket.model_validate(json.loads(path.read_text(encoding="utf-8")))

