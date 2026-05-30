# Building the Dental Context Layer for AI Agents

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

Audience: AI engineers, dental AI builders, healthcare infrastructure developers, and agent/MCP developers.

ClinicBrain is building the Dental Context Layer for AI Agents: a local-first, privacy-first infrastructure layer that transforms dental records into structured Dental Case Packets for dentist-review-only AI workflows.

This is not a diagnostic system. It is not a treatment recommendation system. It is not a medical device. It does not interpret imaging clinically, claim clinical accuracy, or upload patient data.

It is a context layer.

## Why Dental AI Needs A Context Layer

Most dental AI workflows start with a data problem before they ever reach a model problem.

A dental case may include:

- CBCT DICOM studies
- panoramic X-rays
- periapical X-rays
- intraoral scans in STL, PLY, or OBJ
- dental photographs
- clinical notes
- chief complaint text
- treatment plan text

These records are useful to dental teams, but they are awkward for general-purpose LLMs and agent workflows. The files are heterogeneous, large, metadata-heavy, and often mixed with patient identifiers. Even when an AI system should only summarize available records or identify missing information, it still needs a predictable, bounded representation of the case.

That is the gap this project targets.

Dental AI does not only need models. It needs a standardized context layer that can tell an agent what records exist, where they are, what metadata is safe to expose, what information is missing, and what questions should be routed back to a dentist.

## Why Raw Dental Records Are Hard For LLMs

Raw dental records are not naturally LLM-ready.

CBCT and X-ray DICOM files contain imaging pixels, acquisition metadata, and potentially sensitive tags. Intraoral scans may be large mesh files with geometry and sometimes color or material information. Treatment plans and clinical notes may mix useful workflow context with identifiers or free-text ambiguity.

For an LLM or agent, the hard problems are not just reading files. They include:

- detecting what modalities are present
- avoiding PHI exposure
- indexing files without embedding large binary assets
- extracting only safe metadata
- preserving references back to original files
- separating known information from missing information
- keeping all AI-facing outputs non-diagnostic
- making the output portable across different tools

Without a context layer, every agent or workflow has to reinvent this glue.

## What A Dental Case Packet Is

A Dental Case Packet is a structured, portable representation of a dental case.

The v0.1 packet includes:

- a de-identified patient section
- chief complaint text
- clinical notes summary
- treatment plan summary
- CBCT availability and safe DICOM metadata summary
- X-ray file references
- intraoral scan file references and formats
- photo file references
- AI-ready context for clinical review
- missing information
- dentist review questions
- safety flags
- file manifests with SHA-256 hashes
- a Markdown report for human review

The packet does not embed large images or scan files. It references them through manifests and file indexes. This keeps the JSON portable and makes downstream tools more predictable.

The packet is designed for structured data transformation, not clinical decision-making.

## Why MCP Matters

The Model Context Protocol gives AI agents a standard way to call local tools.

For this project, MCP matters because dental records should not need to leave the local environment just so an agent can organize them. A local MCP server can expose constrained tools such as:

- `build_dental_case_packet`
- `validate_case_packet`
- `summarize_packet`
- `list_supported_formats`
- `check_phi_risk`

These tools let an agent build and inspect structured dental context while preserving safety boundaries. The agent does not need raw, unbounded access to every file. It can call explicit tools with explicit outputs.

That is the infrastructure pattern: local records become a Dental Case Packet, the MCP layer exposes safe operations, and AI agents consume structured context.

```text
Dental Records
  -> Dental Case Packet
  -> MCP Layer
  -> AI Agents
```

## Local-first Privacy Model

The reference implementation is local-first by design.

The CLI and MCP tools run on local folders. The package does not call external APIs by default. It does not upload patient data. It does not send DICOM, X-rays, scans, notes, or generated packets to cloud services.

The de-identification approach is allowlist-oriented:

- safe metadata is extracted
- PHI-like DICOM fields are detected and logged without raw values
- de-identified text copies are generated where supported
- large binary assets are referenced, not copied into the packet JSON

This does not replace a formal privacy review. PHI detection is still heuristic. But the architecture is intentionally built around minimizing exposure.

## Safety Boundaries

Every output is for clinical review only.

The project does not:

- diagnose
- recommend treatment
- interpret CBCT or X-rays clinically
- rank treatment options
- claim clinical accuracy
- act as a medical device
- make clinical decisions
- upload patient data

The project does:

- organize records
- de-identify supported inputs
- extract safe metadata
- index files
- build structured packets
- validate schemas
- summarize available and missing records
- generate dentist review questions

The distinction matters. A dental context layer can support AI workflows without becoming a diagnostic system.

## Validation Results

The current validation suite focuses on infrastructure behavior, not clinical accuracy.

Clinical Validation Dataset v0.1 includes 20 representative validation cases. The suite runs through the MCP layer rather than bypassing it.

Results:

- 20 validation cases
- 20/20 packet builds
- 20/20 MCP executions
- 20/20 validation success
- PHI risk low=20

The validation dataset checks whether the pipeline can build packets, validate schemas, summarize records, and run PHI risk checks consistently. It does not test diagnosis. It does not evaluate treatment planning. It does not interpret imaging.

## Release Timeline

### v0.1.0 Developer Preview

The first public developer preview introduced the reference CLI, Dental Case Packet JSON output, Markdown report output, file manifests, DICOM metadata extraction, de-identification behavior, sample inputs and outputs, tests, and GitHub Actions CI.

### v0.1.1 Local MCP Server + Clinical Validation Dataset

This release added the local MCP server wrapper and the first Clinical Validation Dataset v0.1. It introduced MCP tools for building, validating, summarizing, listing formats, and checking PHI risk.

### v0.1.2 Agent-native Adoption Layer

This release added `AGENTS.md`, agent use cases, MCP client configuration docs, agent security guidance, and paste-ready prompts for coding agents and MCP workflows.

### v0.1.3 Discovery and Installation Readiness

This release prepared package metadata, clean wheel install validation, `registry/server.json`, GitHub topics setup guidance, and an adoption readiness review. It prepares the path toward TestPyPI, PyPI, and MCP Registry submission without publishing those channels automatically.

## How Developers Can Try It

Clone the repository:

```bash
git clone https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet.git
cd ai-ready-dental-case-packet
```

Create an environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,mcp]"
```

Build a sample packet:

```bash
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
```

Validate it:

```bash
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

Run the MCP server:

```bash
dental-packet-mcp
```

or:

```bash
python -m dental_packet_mcp
```

Read the agent guide:

```text
AGENTS.md
docs/quick-agent-install.md
docs/mcp-client-config.md
docs/security-for-agents.md
```

## Roadmap

Near-term:

- TestPyPI publication
- PyPI publication
- MCP Registry submission
- stronger local MCP server behavior
- improved package install guidance
- better schema version negotiation

Future:

- DICOM thumbnail service
- treatment plan parser
- dental context evaluation harness
- FHIR interoperability mapping
- OpenAI Agents SDK example
- Claude Desktop example
- Cursor and Codex coding-agent workflow docs
- Dental Context Protocol for AI Agents

## Closing

The goal is not to build a dental chatbot. The goal is to make dental records usable as structured, privacy-first context for AI systems.

If AI agents are going to participate in dental workflows, they need a reliable context layer before they need bigger prompts.

That is what Dental Case Packet is trying to become: DICOM + FHIR + LangChain for dentistry, starting with a local-first reference implementation that keeps clinical review and privacy at the center.
