# PyPI Release Guide

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

This project is prepared for PyPI distribution under the package name `dental-packet`.

The installed console scripts are:

- `dental-packet`
- `dental-packet-mcp`

The package is local-first and does not upload patient data. Publishing to PyPI only distributes the reference implementation and MCP server wrapper.

## Package Metadata

Current package metadata lives in `pyproject.toml`.

Important fields:

- Package name: `dental-packet`
- Console script: `dental-packet`
- MCP console script: `dental-packet-mcp`
- Optional MCP dependencies: `pip install dental-packet[mcp]`
- Development dependencies: `pip install -e ".[dev,mcp]"`

## Build Instructions

From a clean checkout:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip build twine
python -m build
python -m twine check dist/*
```

Expected artifacts:

```text
dist/dental_packet-<version>.tar.gz
dist/dental_packet-<version>-py3-none-any.whl
```

## Upload Instructions

Use TestPyPI first:

```bash
python -m twine upload --repository testpypi dist/*
```

Then install from TestPyPI in a fresh environment and run:

```bash
pip install --index-url https://test.pypi.org/simple/ dental-packet
dental-packet --help
```

For production PyPI:

```bash
python -m twine upload dist/*
```

Use a scoped PyPI API token. Do not store PyPI tokens in this repository.

## Versioning Workflow

1. Update `pyproject.toml` version.
2. Update `CHANGELOG.md`.
3. Run:

```bash
ruff check .
pytest
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
python validation/run_mcp_validation.py
```

4. Build and check the package:

```bash
python -m build
python -m twine check dist/*
```

5. Publish to TestPyPI.
6. Smoke test `dental-packet` and `dental-packet-mcp`.
7. Publish to PyPI.
8. Create the GitHub tag and release.

## MCP Registry Compatibility Note

The MCP Registry verifies PyPI package ownership by checking for an `mcp-name: $SERVER_NAME` string in the PyPI README. Keep the hidden `mcp-name` comment in `README.md` aligned with the server name used in any future `server.json`.

Proposed server name:

```text
io.github.clinicbrain-ai/dental-case-packet-mcp
```

This repository is not published to PyPI yet. Treat the current state as package-ready, not package-published.
