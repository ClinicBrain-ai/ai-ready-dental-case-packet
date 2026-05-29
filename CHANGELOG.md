# Changelog

## v0.1.0 — AI-ready Dental Case Packet Developer Preview

Initial public developer preview for the Dental Case Packet specification and reference CLI.

### Added

- CLI build command: `python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output`.
- CLI validate command: `python -m dental_packet validate --input ./case_packet_output/case_packet.json`.
- Dental Case Packet JSON output: `case_packet.json`.
- Markdown report output: `case_packet.md`.
- File manifest and file index with SHA-256 hashes.
- DICOM metadata extraction for non-sensitive fields.
- PHI-safe metadata handling that logs PHI field presence without exporting raw PHI values.
- Intraoral scan file indexing for STL, PLY, and OBJ files.
- Runnable example input and generated example output.
- Pytest coverage for CLI behavior, schema validation, de-identification, and manifests.
- Ruff validation.
- GitHub Actions CI for ruff, pytest, sample build, and sample validation.

### Safety

- No diagnosis features.
- No treatment recommendation features.
- No clinical accuracy claims.
- Outputs are for dentist review and clinical review workflows only.
