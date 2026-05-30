# Agent Use Cases

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

This document shows safe, local-first workflows for AI agents using the Dental Case Packet project.

Agents must not diagnose, recommend treatment, interpret imaging clinically, upload patient data, or print raw PHI values.

## Use Case 1: Build A Dental Case Packet From A Local Folder

Goal:

Create a structured Dental Case Packet from local records.

Input:

- Local input folder such as `./examples/sample_input`.
- Local output folder such as `./case_packet_output`.

Tool call:

```python
build_dental_case_packet(
    input_folder="./examples/sample_input",
    output_folder="./case_packet_output",
)
```

Expected output:

- `case_packet_path`
- `markdown_report_path`
- `manifest_path`
- `warnings`
- `success`

Safety boundary:

Keep all files local. Do not upload records or generated packets to external services.

## Use Case 2: Validate A Packet

Goal:

Check whether a generated packet matches the current schema.

Input:

- `./case_packet_output/case_packet.json`

Tool call:

```python
validate_case_packet(
    case_packet_path="./case_packet_output/case_packet.json",
)
```

Expected output:

- `valid`
- `errors`
- `warnings`

Safety boundary:

Validation is structural only. Do not treat a valid packet as clinically correct.

## Use Case 3: Check PHI Risk

Goal:

Check for obvious PHI-like fields or patterns without printing raw PHI values.

Input:

- `./case_packet_output/case_packet.json`

Tool call:

```python
check_phi_risk(
    case_packet_path="./case_packet_output/case_packet.json",
)
```

Expected output:

- `risk_level`
- `flagged_fields`
- `recommendations`

Safety boundary:

Report field paths and risk categories only. Never print raw patient identifiers.

## Use Case 4: Summarize Available And Missing Records

Goal:

Return a non-diagnostic summary of available records, missing information, and review questions.

Input:

- `./case_packet_output/case_packet.json`

Tool call:

```python
summarize_packet(
    case_packet_path="./case_packet_output/case_packet.json",
)
```

Expected output:

- `case_overview`
- `available_records`
- `missing_information`
- `dentist_review_questions`
- `safety_disclaimer`

Safety boundary:

Summaries are for clinical review only. Do not infer diagnoses or suggest treatment.

## Use Case 5: Use MCP Tools From An AI Agent

Goal:

Expose Dental Case Packet operations to an MCP-compatible local AI agent.

Input:

- MCP server command: `python -m dental_packet_mcp`
- Local case folders.

Tool call:

```json
{
  "tool": "build_dental_case_packet",
  "arguments": {
    "input_folder": "./examples/sample_input",
    "output_folder": "./case_packet_output"
  }
}
```

Expected output:

- Structured JSON tool result.
- Local packet files.

Safety boundary:

The agent should call MCP tools only for local structured transformation. Do not chain the result into external upload or diagnosis tools.

## Use Case 6: Use This Repository As A Dental Context Layer

Goal:

Use Dental Case Packets as the context layer in a larger agent workflow.

Input:

- Local Dental Case Packet JSON.
- Manifest references.
- Markdown report.
- PHI risk result.

Tool call:

```python
summary = summarize_packet("./case_packet_output/case_packet.json")
phi_risk = check_phi_risk("./case_packet_output/case_packet.json")
```

Expected output:

- A structured context object.
- A safety disclaimer.
- Missing-information list.
- Review questions for a dentist.

Safety boundary:

Downstream agents must preserve privacy-first, dentist-review-only, non-diagnostic behavior. Do not convert packet context into clinical decisions.
