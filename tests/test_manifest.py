from __future__ import annotations

import hashlib

from dental_packet.file_indexer import build_file_index


def test_manifest_hash_correct(tmp_path) -> None:
    input_root = tmp_path / "project-input"
    input_root.mkdir()
    source = input_root / "treatment_plan.txt"
    source.write_text("Phase 1: collect records.", encoding="utf-8")

    manifest = build_file_index(input_root)

    assert len(manifest) == 1
    assert manifest[0].sha256 == hashlib.sha256(b"Phase 1: collect records.").hexdigest()
    assert manifest[0].role == "treatment_plan"

