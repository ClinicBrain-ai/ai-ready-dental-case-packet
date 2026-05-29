# v0.1.3 — Discovery and Installation Readiness

`ai-ready-dental-case-packet` is Building the Dental Context Layer for AI Agents.

This controlled release prepares the project for discovery, installation, and future registry adoption without publishing to PyPI or submitting to the MCP Registry yet.

The project remains local-first, privacy-first, and dentist-review-only. It does not diagnose, does not recommend treatment, does not interpret imaging clinically, and does not upload patient data.

## What's New

### PyPI Packaging Readiness

- Prepared package metadata for `dental-packet`.
- Confirmed console scripts:
  - `dental-packet`
  - `dental-packet-mcp`
- Updated package metadata with keywords, classifiers, project URLs, and SPDX license format.
- Verified local build produces both source distribution and wheel artifacts.

### Clean Wheel Install Validation

- Built `dental_packet-0.1.2.tar.gz`.
- Built `dental_packet-0.1.2-py3-none-any.whl`.
- Installed the wheel into a clean temporary virtual environment.
- Verified:
  - `dental-packet --help`
  - `dental-packet-mcp --help`
  - sample build command
  - sample validate command

### MCP Registry Preparation

- Added `registry/server.json`.
- Validated `registry/server.json` against the official MCP Registry `2025-12-11` JSON schema.
- Documented schema-supported fields and publisher metadata limitations.
- Kept MCP Registry submission as a later controlled phase.

### GitHub Topics Setup Guide

- Added manual GitHub topic setup instructions for:
  - `mcp`
  - `model-context-protocol`
  - `ai-agents`
  - `agent-tools`
  - `dental-ai`
  - `cbct`
  - `dicom`
  - `healthcare-ai`
  - `llm-tools`
  - `context-layer`
  - `agent-infrastructure`

### Adoption Readiness Review

- Updated adoption readiness assessment.
- Raised overall readiness from `7.7/10` to `8.4/10`.
- Documented remaining blockers before TestPyPI, PyPI, and MCP Registry submission.

## Safety Boundaries

- No diagnosis.
- No treatment recommendations.
- No clinical interpretation.
- No clinical accuracy claims.
- No patient data upload behavior.
- Local-first execution.
- Dentist-review-only outputs.

## Not Included

This release does not publish to:

- TestPyPI
- PyPI
- MCP Registry

Those steps remain controlled follow-up phases requiring explicit maintainer approval.

## Validation

Validated before release:

- `ruff check .`
- `pytest`
- `python -m build`
- `python -m twine check dist/*`
- clean wheel install smoke test
- sample build command
- sample validate command
- MCP validation suite
