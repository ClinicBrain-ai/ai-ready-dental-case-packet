# GitHub Discussions Announcement

## Building the Dental Context Layer for AI Agents

We have been preparing `ai-ready-dental-case-packet` as a local-first infrastructure project for dental AI workflows.

The goal is not diagnosis, treatment recommendation, or clinical decision support.

The goal is structured context.

Dental Case Packet turns local dental records into a portable, privacy-first packet that AI agents and clinical review workflows can inspect safely:

- CBCT DICOM metadata summaries
- X-ray file references
- intraoral scan references
- photo references
- clinical notes summaries
- treatment plan summaries
- missing information
- dentist review questions
- file manifests with hashes
- non-diagnostic AI context

The project now includes:

- CLI build and validate commands
- local MCP server
- MCP tools for build, validate, summarize, list formats, and PHI risk
- Clinical Validation Dataset v0.1
- 20 validation cases
- 20/20 packet builds
- 20/20 MCP executions
- 20/20 validation success
- PHI risk low=20
- AGENTS.md for coding agents
- MCP client config docs
- package metadata and `registry/server.json`

Safety boundaries:

- no diagnosis
- no treatment recommendations
- no clinical interpretation
- no patient data upload
- local-first
- privacy-first
- dentist-review-only
- not a medical device

Try it locally:

```bash
git clone https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet.git
cd ai-ready-dental-case-packet
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,mcp]"
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
python -m dental_packet_mcp
```

Feedback wanted:

- Does the packet schema cover the right dental context?
- What metadata should be normalized next?
- How should MCP clients discover local dental context tools?
- What should the evaluation harness measure?

Repo:
https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet
