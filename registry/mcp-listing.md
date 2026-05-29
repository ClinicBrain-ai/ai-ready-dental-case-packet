# Dental Case Packet MCP

Short description:

Local-first Dental Context Layer for AI Agents.

## Overview

Dental Case Packet MCP helps AI agents transform local dental records into structured Dental Case Packets for clinical review and AI workflows.

It is designed for privacy-first infrastructure workflows where dental teams, developers, and AI agents need standardized dental context without diagnosis or treatment recommendations.

## Capabilities

- Build dental case packets.
- Validate packets.
- Summarize packets.
- Check PHI risk.

## Supported Inputs

- CBCT DICOM
- X-ray DICOM/JPG/PNG
- Intraoral scan STL/PLY/OBJ
- Photos JPG/PNG
- Text notes TXT

## Safety

- No diagnosis.
- No treatment recommendations.
- No clinical interpretation.
- Privacy-first.
- Local execution.
- Dentist-review-only outputs.

## Install

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

## Repository

https://github.com/ClinicBrain-ai/ai-ready-dental-case-packet
