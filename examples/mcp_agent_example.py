from __future__ import annotations

from pathlib import Path

from dental_packet_mcp.core import (
    build_dental_case_packet,
    check_phi_risk,
    list_supported_formats,
    summarize_packet,
    validate_case_packet,
)


def main() -> None:
    """Demonstrate local MCP tool behavior without sending data to external APIs."""
    repo_root = Path(__file__).resolve().parents[1]
    input_folder = repo_root / "examples" / "sample_input"
    output_folder = repo_root / "case_packet_output"

    build_result = build_dental_case_packet(
        input_folder=input_folder.as_posix(),
        output_folder=output_folder.as_posix(),
    )
    print("build_dental_case_packet:", build_result)

    case_packet_path = build_result["case_packet_path"]
    print("validate_case_packet:", validate_case_packet(case_packet_path))
    print("summarize_packet:", summarize_packet(case_packet_path))
    print("check_phi_risk:", check_phi_risk(case_packet_path))
    print("list_supported_formats:", list_supported_formats())


if __name__ == "__main__":
    main()
