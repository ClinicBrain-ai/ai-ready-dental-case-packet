# Quick Agent Install

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

This guide shows how to install and configure Dental Case Packet MCP for local AI agent workflows.

The server is local-first. It does not upload patient data, diagnose, recommend treatment, or interpret imaging clinically.

## Install

From a local checkout:

```bash
git clone https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet.git
cd ai-ready-dental-case-packet
python -m venv .venv
source .venv/bin/activate
pip install -e ".[mcp]"
```

Future PyPI install:

```bash
pip install "dental-packet[mcp]"
```

## Run

```bash
dental-packet-mcp
```

Alternative:

```bash
python -m dental_packet_mcp
```

## Claude Desktop

Example configuration:

```json
{
  "mcpServers": {
    "dental-case-packet": {
      "command": "python",
      "args": ["-m", "dental_packet_mcp"],
      "cwd": "/absolute/path/to/ai-ready-dental-case-packet"
    }
  }
}
```

Agent instruction:

```text
Use Dental Case Packet MCP only for local structured dental data transformation. Do not diagnose, recommend treatment, interpret imaging clinically, upload patient data, or print raw PHI values.
```

## Cursor

Example MCP configuration:

```json
{
  "mcpServers": {
    "dental-case-packet": {
      "command": "dental-packet-mcp",
      "args": [],
      "cwd": "/absolute/path/to/ai-ready-dental-case-packet"
    }
  }
}
```

## Codex

Use this repository as a local workspace.

Recommended prompt:

```text
Read AGENTS.md first. Use the dental-packet CLI or dental-packet-mcp server only for local Dental Case Packet workflows. Do not diagnose, recommend treatment, interpret imaging clinically, upload patient data, or print raw PHI values.
```

Useful commands:

```bash
ruff check .
pytest
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
python validation/run_mcp_validation.py
```

## Generic MCP Client

```json
{
  "name": "dental-case-packet",
  "transport": "stdio",
  "command": "python",
  "args": ["-m", "dental_packet_mcp"],
  "cwd": "/absolute/path/to/ai-ready-dental-case-packet"
}
```

## Smoke Test

```bash
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

Expected output:

```text
Built case packet: case_packet_output/case_packet.json
case_packet.json is valid
```
