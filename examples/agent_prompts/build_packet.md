# Prompt: Build A Dental Case Packet

You are helping me use `ai-ready-dental-case-packet` as a local-first Dental Context Layer.

Goal:

Build a Dental Case Packet from a local input folder.

Input folder:

```text
./project-input
```

Output folder:

```text
./case_packet_output
```

Instructions:

1. Do not diagnose.
2. Do not recommend treatment.
3. Do not interpret imaging clinically.
4. Do not upload patient data anywhere.
5. Keep all processing local.
6. Use the CLI or MCP tool only for structured data transformation.

Preferred command:

```bash
python -m dental_packet build --input ./project-input --output ./case_packet_output
```

If MCP is available, use:

```json
{
  "tool": "build_dental_case_packet",
  "arguments": {
    "input_folder": "./project-input",
    "output_folder": "./case_packet_output"
  }
}
```

After building, report only:

- Whether the build succeeded.
- The generated file paths.
- Any warnings.
- A reminder that outputs are for clinical review only.
