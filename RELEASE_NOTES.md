# v0.1.0 — AI-ready Dental Case Packet Developer Preview

ClinicBrain is releasing the first developer preview of `ai-ready-dental-case-packet`, an infrastructure project for turning dental records into structured, privacy-first Dental Case Packets.

This release is designed for dental teams, developers, and AI workflow builders who need a local, inspectable way to prepare dental records for clinical review and AI context pipelines.

This is not a diagnostic AI system. It does not recommend treatment and does not claim clinical accuracy.

## What Is Included

- Dental Case Packet Specification v0.1.
- Local Python CLI for building packets.
- CLI validation for generated `case_packet.json` files.
- Structured JSON output.
- Markdown report output.
- File manifest and file index with SHA-256 hashes.
- DICOM metadata extraction for non-sensitive metadata.
- PHI-safe metadata handling that avoids exporting raw PHI values.
- Intraoral scan file indexing for STL, PLY, and OBJ files.
- Runnable sample input and sample output.
- Pytest test coverage.
- Ruff linting.
- GitHub Actions CI for release checks.

## How To Try It

```bash
git clone https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet.git
cd ai-ready-dental-case-packet

python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

Expected output:

```text
Built case packet: case_packet_output/case_packet.json
case_packet.json is valid
```

## Known Limitations

- This is a developer preview, not a production clinical system.
- DICOM support is metadata-focused; there is no viewer in v0.1.0.
- Intraoral scan support is limited to file indexing and best-effort mesh metadata.
- PDF ingestion is not implemented yet.
- No LLM API calls are included in the reference CLI.
- No diagnosis, treatment recommendation, or automated clinical interpretation is included.
- De-identification is implemented with conservative local rules and should be reviewed before use with real patient data.

## Roadmap

- DICOM thumbnail service.
- Treatment plan parser.
- Dental Context Builder improvements.
- FHIR interoperability mapping.
- Optional OpenAI connector.
- Dental RAG patterns.
- Dental Agent SDK.
- AI-native dental infrastructure platform.

## Safety Disclaimer

Dental Case Packets are structured context artifacts for review workflows. They are not medical advice, diagnosis, treatment planning, or clinical decision support. All generated outputs must be reviewed by qualified dental professionals before any clinical use.
