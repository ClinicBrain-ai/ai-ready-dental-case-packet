from __future__ import annotations

import json
from pathlib import Path


def test_clinical_validation_dataset_v0_1_artifacts_exist() -> None:
    root = Path("validation")
    manifest = json.loads((root / "validation_manifest.json").read_text(encoding="utf-8"))

    assert manifest["name"] == "Clinical Validation Dataset v0.1"
    assert manifest["total_cases"] >= 20
    assert len(manifest["cases"]) >= 20

    for case in manifest["cases"]:
        case_id = case["case_id"]
        assert (root / "cases" / case_id / "clinical_notes.txt").exists()
        assert (root / "packet_outputs" / case_id / "case_packet.json").exists()
        assert (root / "packet_outputs" / case_id / "case_packet.md").exists()
        assert (root / "mcp_outputs" / case_id / "mcp_summary.json").exists()
        assert (root / "mcp_outputs" / case_id / "phi_risk_report.json").exists()
        assert (root / "reports" / f"{case_id}.md").exists()
        assert case["build_success"] is True
        assert case["validation_success"] is True
        assert case["mcp_success"] is True
        assert case["phi_risk_level"] == "low"

    validation_report = (root / "validation_report.md").read_text(encoding="utf-8")
    benchmark_summary = (root / "benchmark_summary.md").read_text(encoding="utf-8")
    assert "Total cases: 20" in validation_report
    assert "No diagnosis, treatment recommendation, or clinical interpretation" in benchmark_summary
