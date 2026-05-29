# Check PHI Risk Through MCP

You are working in the `ai-ready-dental-case-packet` repository.

Goal:
Check a generated Dental Case Packet for obvious PHI risk without printing any raw PHI values.

Input:
- Case packet path: `./case_packet_output/case_packet.json`

Required tool:
- Use the MCP tool `check_phi_risk`.

Instructions:
1. Call `check_phi_risk` with the packet path.
2. Report only:
   - risk level
   - flagged field names
   - recommendations
3. Do not print raw values from the packet.
4. Do not upload the packet or send patient data to an external API.

Safety boundary:
This is privacy screening for infrastructure validation only. Do not diagnose, interpret imaging, or recommend treatment.
