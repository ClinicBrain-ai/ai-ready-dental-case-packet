# AGENTS.md

This file is the operating guide for AI coding agents working in this repository.

## Project Mission

This repository is now framed as the Clinical Cognition Transformation Lab
(CCTL).

CCTL studies Human-AI Clinical Cognition: the distributed cognitive processes
that emerge when clinical decisions are jointly produced by clinicians, AI
systems, documentation artifacts, institutional workflows, healthcare
organizations, patients, and caregivers.

The historical `ai-ready-dental-case-packet` package remains the original
technical substrate: a local-first Dental Case Packet builder and
MCP-compatible tool layer. Preserve working CLI, MCP, tests, schemas, examples,
and validation code unless explicitly asked to change them.

Public-facing documentation should lead with CCTL, Clinical Cognition
Transformation, Human-AI Clinical Cognition, Cognitive Provenance, Cognitive
Reconstruction, Longitudinal Cognitive Change, and Human-AI Co-Cognition.

DCS and dental packet materials should be described as origins or downstream
research artifacts, not as the central research question.

## What This Project Is Not

This project is not:

- A diagnostic system.
- A treatment recommendation system.
- A medical device.
- A clinical decision system.
- A cloud upload service.
- A dental chatbot.

## Architecture Overview

```text
src/dental_packet/
  CLI and reference implementation
  DICOM metadata extraction
  de-identification helpers
  file indexing
  scan parsing
  schema validation
  Markdown report writing

src/dental_packet_mcp/
  local MCP-compatible tool layer
  build/validate/summarize/PHI-risk tools

spec/
  Dental Case Packet specification artifacts

docs/
  architecture, quickstart, MCP, security, positioning, release docs

examples/
  sample input/output and agent prompts

validation/
  Clinical Validation Dataset v0.1
  packet outputs, MCP outputs, per-case reports, aggregate reports
```

## Setup Commands

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

For MCP server work:

```bash
pip install -e ".[dev,mcp]"
```

## Test Commands

```bash
ruff check .
pytest
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
python validation/run_mcp_validation.py
```

## CLI Commands

Build a packet:

```bash
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
```

Validate a packet:

```bash
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

## MCP Server Commands

Run the MCP server:

```bash
python -m dental_packet_mcp
```

or:

```bash
dental-packet-mcp
```

MCP tools:

- `build_dental_case_packet`
- `validate_case_packet`
- `summarize_packet`
- `list_supported_formats`
- `check_phi_risk`

## Safety Boundaries

Agents must preserve these boundaries:

- Keep all workflows local-first.
- Do not upload patient data.
- Do not call external APIs with case data.
- Do not diagnose.
- Do not recommend treatment.
- Do not claim clinical accuracy.
- Do not interpret imaging clinically.
- Do not print raw PHI values.
- Mark AI-facing outputs as for clinical review only.

## Prohibited Behaviors

Do not add code or docs that:

- Makes diagnostic claims.
- Suggests treatment plans or treatment ranking.
- Converts generated summaries into clinical decisions.
- Automatically uploads files to cloud services.
- Sends DICOM, X-rays, scans, notes, or packets to external APIs.
- Executes shell commands from case files or metadata.
- Treats untrusted DICOM metadata or notes as instructions.

## Expected Contribution Style

- Prefer small, local-first changes.
- Reuse existing schema and CLI patterns.
- Add tests for behavior changes.
- Keep outputs deterministic where practical.
- Keep generated packet files reference-based; do not embed large imaging assets.
- Use allowlists for de-identification and metadata export.
- Document limitations clearly.
- Preserve dentist-review-only language.

## Where To Look

- Specification: `spec/dental-case-packet-v0.1.md`
- JSON Schema: `spec/dental-case-packet.schema.json`
- CLI implementation: `src/dental_packet/cli.py`
- MCP tools: `src/dental_packet_mcp/core.py`
- MCP server docs: `docs/mcp-server.md`
- Agent use cases: `docs/agent-use-cases.md`
- MCP client configs: `docs/mcp-client-config.md`
- Agent security guidance: `docs/security-for-agents.md`
- Example prompts: `examples/agent_prompts/`
- Sample input: `examples/sample_input/`
- Sample output: `examples/sample_output/`
- Validation report: `validation/validation_report.md`
- Benchmark summary: `validation/benchmark_summary.md`

## Final Reminder

This repository is infrastructure. It prepares structured dental context. It does not provide diagnosis, treatment recommendations, medical advice, or clinical decisions.
