# Prompt: Validate A Dental Case Packet

You are helping me validate a generated Dental Case Packet.

Packet path:

```text
./case_packet_output/case_packet.json
```

Instructions:

1. Validate schema and structural correctness only.
2. Do not diagnose.
3. Do not recommend treatment.
4. Do not judge clinical accuracy.
5. Do not send the packet to external APIs.

Preferred command:

```bash
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

If MCP is available, use:

```json
{
  "tool": "validate_case_packet",
  "arguments": {
    "case_packet_path": "./case_packet_output/case_packet.json"
  }
}
```

Return:

- `valid`
- schema errors, if any
- warnings, if any
- a reminder that structural validity is not clinical validity
