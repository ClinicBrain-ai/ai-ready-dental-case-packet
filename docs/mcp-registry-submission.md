# MCP Registry Submission Preparation

The MCP Registry is the discovery layer for publicly accessible MCP servers. Current official documentation describes it as a centralized metadata repository that stores standardized `server.json` metadata, including a unique server name, package location, execution instructions, and server capabilities.

Sources reviewed:

- https://modelcontextprotocol.io/registry/about
- https://modelcontextprotocol.io/registry/quickstart
- https://modelcontextprotocol.io/registry/package-types
- https://modelcontextprotocol.io/registry/faq

The registry is currently in preview, so submission details may change.

## Proposed Server

Title:

```text
Dental Case Packet MCP
```

Proposed server name:

```text
io.github.clinicbrain-ai/dental-case-packet-mcp
```

Short description:

```text
Local-first Dental Context Layer for AI Agents.
```

Package:

```text
dental-packet
```

Command:

```bash
dental-packet-mcp
```

Alternative command:

```bash
python -m dental_packet_mcp
```

## Server Description

Dental Case Packet MCP exposes local tools that transform dental records into structured, privacy-first Dental Case Packets for clinical review and AI workflows.

It is infrastructure for AI agents. It is not a diagnostic system, treatment recommendation system, medical device, clinical decision system, or cloud upload service.

## Capabilities

- Build Dental Case Packets from local input folders.
- Validate generated `case_packet.json` files.
- Return non-diagnostic summaries of available and missing records.
- List supported dental record formats.
- Check obvious PHI risk without printing raw PHI values.

## Tool Definitions

### `build_dental_case_packet`

Input:

- `input_folder`: local folder containing dental records.
- `output_folder`: local destination folder.

Output:

- `success`
- `case_packet_path`
- `markdown_report_path`
- `manifest_path`
- `warnings`

### `validate_case_packet`

Input:

- `case_packet_path`: local path to `case_packet.json`.

Output:

- `valid`
- `errors`
- `warnings`

### `summarize_packet`

Input:

- `case_packet_path`: local path to `case_packet.json`.

Output:

- `case_overview`
- `available_records`
- `missing_information`
- `dentist_review_questions`
- `safety_disclaimer`

### `list_supported_formats`

Output:

- CBCT/DICOM
- X-ray DICOM/JPG/PNG
- intraoral scan STL/PLY/OBJ
- photos JPG/PNG
- text notes TXT

### `check_phi_risk`

Input:

- `case_packet_path`: local path to `case_packet.json`.

Output:

- `risk_level`
- `flagged_fields`
- `recommendations`

## Safety Boundaries

- No diagnosis.
- No treatment recommendations.
- No clinical interpretation.
- No clinical accuracy claims.
- No cloud upload behavior.
- No external API calls with patient data.
- No raw PHI values in PHI risk output.
- Dentist-review-only outputs.

## Local-first Architecture

```text
Local dental records
  -> dental-packet reference pipeline
  -> Dental Case Packet JSON/Markdown/manifest
  -> dental-packet-mcp local MCP tools
  -> AI agent receives structured references and summaries
```

Patient data remains on the local machine unless a human operator explicitly shares files outside this repository.

## Installation Instructions

Editable install:

```bash
pip install -e ".[mcp]"
dental-packet-mcp
```

Future PyPI install:

```bash
pip install "dental-packet[mcp]"
dental-packet-mcp
```

## Draft `server.json`

This draft should be validated against the current MCP Registry schema before submission.

```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.clinicbrain-ai/dental-case-packet-mcp",
  "title": "Dental Case Packet MCP",
  "description": "Local-first Dental Context Layer for AI Agents.",
  "repository": {
    "url": "https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet",
    "source": "github"
  },
  "version": "0.1.2",
  "packages": [
    {
      "registryType": "pypi",
      "identifier": "dental-packet",
      "version": "0.1.2",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

## Submission Checklist

- [ ] Publish `dental-packet` to PyPI.
- [ ] Confirm the PyPI README includes `mcp-name: io.github.clinicbrain-ai/dental-case-packet-mcp`.
- [ ] Install `mcp-publisher`.
- [ ] Generate or validate `server.json`.
- [ ] Authenticate with the MCP Registry.
- [ ] Publish with `mcp-publisher publish`.
- [ ] Verify the listing through the MCP Registry API.

## Draft MCP Registry Listing Copy

Dental Case Packet MCP is a local-first MCP server for AI agents that need to transform dental records into structured Dental Case Packets. It supports CBCT DICOM, dental X-rays, intraoral scans, photos, and text notes through a privacy-first pipeline that builds JSON packets, Markdown reports, manifests, and PHI-safe summaries.

This server is for structured data transformation only. It does not diagnose, recommend treatment, interpret imaging clinically, claim clinical accuracy, or upload patient data.
