# v0.1.0 Release Checklist

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

Release: `v0.1.0 — AI-ready Dental Case Packet Developer Preview`

## Local Verification

- [x] `ruff check .` passed.
- [x] `pytest` passed.
- [x] Build command works:
  `python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output`.
- [x] Validate command works:
  `python -m dental_packet validate --input ./case_packet_output/case_packet.json`.

## Examples

- [x] Sample input exists at `examples/sample_input/`.
- [x] Sample output exists at `examples/sample_output/`.
- [x] Sample outputs do not contain raw PHI.
- [x] `case_packet.json` follows the v0.1 schema.
- [x] Manifest includes SHA-256 hashes.
- [x] Markdown report is generated.

## CI And Release

- [x] GitHub Actions CI workflow exists.
- [ ] CI passes on GitHub.
- [ ] GitHub release tag `v0.1.0` created.
- [ ] Release notes published.

## Safety

- [x] No diagnosis features added.
- [x] No treatment recommendation features added.
- [x] No clinical accuracy claims added.
- [x] Outputs remain dentist-review-only and privacy-first.
