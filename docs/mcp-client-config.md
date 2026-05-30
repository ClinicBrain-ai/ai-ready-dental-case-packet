# MCP Client Configuration

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

This project exposes a local MCP server for Dental Case Packet workflows.

The server is local-first and privacy-first. It does not send patient data to external APIs, does not diagnose, and does not recommend treatment.

## Commands

Use either command:

```bash
dental-packet-mcp
```

or:

```bash
python -m dental_packet_mcp
```

Install MCP dependencies first:

```bash
pip install -e ".[mcp]"
```

## Claude Desktop

Example `claude_desktop_config.json` entry:

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

Alternative if the console script is on your PATH:

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

## Cursor

Example local MCP configuration:

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
Use the dental-case-packet MCP server only for local structured transformation.
Do not upload patient data. Do not diagnose. Do not recommend treatment.
```

## OpenAI Agents SDK Style Usage

Conceptual local configuration:

```python
from agents import Agent
from agents.mcp import MCPServerStdio

dental_packet_server = MCPServerStdio(
    name="dental-case-packet",
    command="python",
    args=["-m", "dental_packet_mcp"],
    cwd="/absolute/path/to/ai-ready-dental-case-packet",
)

agent = Agent(
    name="Dental Context Builder",
    instructions=(
        "Use local Dental Case Packet MCP tools for structured data transformation only. "
        "Do not diagnose, recommend treatment, or send patient data to external APIs."
    ),
    mcp_servers=[dental_packet_server],
)
```

This is an integration pattern, not a requirement to call an external API with case data.

## Generic Local MCP Client

```json
{
  "name": "dental-case-packet",
  "transport": "stdio",
  "command": "python",
  "args": ["-m", "dental_packet_mcp"],
  "cwd": "/absolute/path/to/ai-ready-dental-case-packet"
}
```

## Exposed Tools

- `build_dental_case_packet`
- `validate_case_packet`
- `summarize_packet`
- `list_supported_formats`
- `check_phi_risk`

## Safety Notes

- Keep case folders local.
- Review outputs before sharing.
- Do not connect generated packet content to diagnosis or treatment tools.
- Do not paste raw PHI into chat prompts.
- Do not configure automatic upload steps.
