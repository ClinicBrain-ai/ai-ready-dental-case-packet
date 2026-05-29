from __future__ import annotations

from dental_packet_mcp.core import (
    build_dental_case_packet,
    check_phi_risk,
    list_supported_formats,
    summarize_packet,
    validate_case_packet,
)


def create_server():
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:
        raise RuntimeError(
            "The MCP server dependencies are not installed. "
            'Install them with: pip install -e ".[mcp]"'
        ) from exc

    mcp = FastMCP("ai-ready-dental-case-packet")
    mcp.tool()(build_dental_case_packet)
    mcp.tool()(validate_case_packet)
    mcp.tool()(summarize_packet)
    mcp.tool()(list_supported_formats)
    mcp.tool()(check_phi_risk)
    return mcp


def main() -> None:
    create_server().run()


if __name__ == "__main__":
    main()
