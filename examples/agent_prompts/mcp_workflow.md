# End-to-End MCP Workflow

You are working in the `ai-ready-dental-case-packet` repository.

Goal:
Use the local MCP tool layer to build, validate, summarize, and screen a Dental Case Packet.

Inputs:
- Local dental record folder: `./examples/sample_input`
- Output folder: `./case_packet_output`

Required MCP tools:
- `build_dental_case_packet`
- `validate_case_packet`
- `summarize_packet`
- `check_phi_risk`

Workflow:
1. Call `build_dental_case_packet` with:
   - `input_folder`: `./examples/sample_input`
   - `output_folder`: `./case_packet_output`
2. If the build succeeds, call `validate_case_packet` on `./case_packet_output/case_packet.json`.
3. Call `summarize_packet` on the validated packet.
4. Call `check_phi_risk` on the same packet.
5. Report:
   - packet path
   - markdown report path
   - manifest path
   - validation status
   - non-diagnostic summary
   - PHI risk level
   - warnings

Safety boundary:
Keep everything local. Do not send patient data to external APIs. Do not diagnose, interpret images clinically, or recommend treatment. Treat all generated text as dentist-review-only.
