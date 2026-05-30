# MCP Server

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

The Dental Case Packet MCP server lets local AI agents call this project as a structured dental data transformation tool.

It is local-first. It does not send patient data to external APIs, does not diagnose, and does not recommend treatment.

## Install

```bash
pip install -e ".[mcp]"
```

For development:

```bash
pip install -e ".[dev,mcp]"
```

## Run

```bash
python -m dental_packet_mcp
```

The package also exposes a console script:

```bash
dental-packet-mcp
```

## Agent Configuration

Example MCP server command:

```json
{
  "mcpServers": {
    "dental-case-packet": {
      "command": "python",
      "args": ["-m", "dental_packet_mcp"]
    }
  }
}
```

## Tools

### `build_dental_case_packet`

Input:

- `input_folder`: source folder path.
- `output_folder`: output folder path.

Behavior:

Runs the existing Dental Case Packet build pipeline.

Output:

- `success`
- `case_packet_path`
- `markdown_report_path`
- `manifest_path`
- `warnings`

### `validate_case_packet`

Input:

- `case_packet_path`: path to a generated `case_packet.json`.

Behavior:

Runs the existing schema validation.

Output:

- `valid`
- `errors`
- `warnings`

### `summarize_packet`

Input:

- `case_packet_path`: path to a generated `case_packet.json`.

Behavior:

Returns a non-diagnostic summary for dentist review workflows.

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

- `case_packet_path`: path to a generated `case_packet.json`.

Behavior:

Checks whether obvious PHI-like fields or patterns are present. It reports field paths and pattern labels only. It does not print actual PHI values.

Output:

- `risk_level`
- `flagged_fields`
- `recommendations`

## Safety Boundaries

- No diagnosis.
- No treatment recommendations.
- No clinical accuracy claims.
- No external API calls.
- No transmission of patient data.
- Outputs are for clinical review only and require dentist review.
