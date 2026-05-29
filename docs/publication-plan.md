# Publication Plan

This document defines the controlled rollout path for discovery and installation.

Positioning:

```text
Building the Dental Context Layer for AI Agents.
```

Safety boundaries:

- No diagnosis.
- No treatment recommendations.
- No clinical interpretation.
- No patient data upload behavior.
- Local-first and dentist-review-only outputs.

## Phase 1: GitHub v0.1.3 Release

Goal:

Publish release notes and a GitHub tag without publishing package artifacts to PyPI or submitting to the MCP Registry.

Commands:

```bash
git status --short --branch
ruff check .
pytest
python -m build
python -m twine check dist/*
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
python validation/run_mcp_validation.py

git add CHANGELOG.md RELEASE_NOTES_v0.1.3.md docs/publication-plan.md
git commit -m "Prepare v0.1.3 discovery release"
git push origin main
git tag v0.1.3
git push origin v0.1.3
```

Required credentials:

- GitHub push access.
- GitHub Release publishing access.

Rollback notes:

- If the tag is pushed but release publishing fails, keep the tag and create the release manually from the GitHub UI.
- If the tag points to the wrong commit and has not been used publicly, delete and recreate only with maintainer approval.

Validation checklist:

- [ ] GitHub main contains release commit.
- [ ] Tag `v0.1.3` points to the release commit.
- [ ] Release notes are published.
- [ ] No PyPI upload occurred.
- [ ] No MCP Registry submission occurred.

## Phase 2: TestPyPI Publication

Goal:

Validate public package installation from TestPyPI before production PyPI.

Commands:

```bash
rm -rf dist build src/dental_packet.egg-info
python -m build
python -m twine check dist/*
python -m twine upload --repository testpypi dist/*

python -m venv /tmp/dental-packet-testpypi
/tmp/dental-packet-testpypi/bin/python -m pip install --upgrade pip
/tmp/dental-packet-testpypi/bin/python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  "dental-packet[mcp]"

/tmp/dental-packet-testpypi/bin/dental-packet --help
/tmp/dental-packet-testpypi/bin/dental-packet-mcp --help
```

Required credentials:

- TestPyPI account.
- TestPyPI API token scoped to `dental-packet` if available.

Rollback notes:

- TestPyPI files are immutable. If a package version is wrong, publish a new version.
- Do not reuse a failed version number for production if metadata differs materially.

Validation checklist:

- [ ] TestPyPI upload succeeds.
- [ ] Install from TestPyPI succeeds.
- [ ] CLI help works.
- [ ] MCP help works.
- [ ] Sample build/validate works from installed package.

## Phase 3: PyPI Publication

Goal:

Publish `dental-packet` to production PyPI.

Commands:

```bash
rm -rf dist build src/dental_packet.egg-info
python -m build
python -m twine check dist/*
python -m twine upload dist/*

python -m venv /tmp/dental-packet-pypi
/tmp/dental-packet-pypi/bin/python -m pip install --upgrade pip
/tmp/dental-packet-pypi/bin/python -m pip install "dental-packet[mcp]"
/tmp/dental-packet-pypi/bin/dental-packet --help
/tmp/dental-packet-pypi/bin/dental-packet-mcp --help
```

Required credentials:

- PyPI account.
- PyPI API token scoped to `dental-packet`.

Rollback notes:

- PyPI files are immutable and should not be deleted casually.
- If a release is broken, publish a patch version and mark the broken version clearly in release notes.

Validation checklist:

- [ ] PyPI upload succeeds.
- [ ] Install from PyPI succeeds.
- [ ] CLI help works.
- [ ] MCP help works.
- [ ] Sample build/validate works from installed package.

## Phase 4: MCP Registry Submission

Goal:

Submit `registry/server.json` after the PyPI package is publicly available.

Commands:

```bash
mcp-publisher --help
mcp-publisher login github
mcp-publisher publish registry/server.json
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.clinicbrain-ai/dental-case-packet-mcp"
```

Required credentials:

- GitHub account authorized for the `ClinicBrain-ai` namespace.
- MCP Registry publisher authentication.
- Published PyPI package `dental-packet`.

Rollback notes:

- MCP Registry version metadata is expected to be immutable.
- If metadata is wrong, publish a new unique version.
- Do not submit until PyPI installation has been validated.

Validation checklist:

- [ ] `registry/server.json` validates against the current schema.
- [ ] PyPI package exists.
- [ ] README includes `mcp-name: io.github.clinicbrain-ai/dental-case-packet-mcp`.
- [ ] MCP Registry publish succeeds.
- [ ] Registry API search returns the server.

## Phase 5: Agent Ecosystem Discovery

Goal:

Improve discovery through GitHub search, package managers, MCP aggregators, and future agent marketplaces.

Commands:

```bash
git status --short --branch
python -m dental_packet build --input ./examples/sample_input --output ./case_packet_output
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

Manual steps:

- Apply GitHub topics from `docs/github-topics-setup.md`.
- Link to `AGENTS.md` from marketplace listing copy where supported.
- Link to `docs/quick-agent-install.md` from package and registry pages.
- Monitor issues for install failures and MCP client compatibility reports.

Required credentials:

- GitHub repository maintainer access.
- Access to any future agent marketplace publisher accounts.

Rollback notes:

- GitHub topics and descriptions can be edited.
- Marketplace listings should be paused or updated if install instructions break.

Validation checklist:

- [ ] GitHub topics applied.
- [ ] README first 30 seconds remains clear.
- [ ] Agent install docs remain current.
- [ ] Safety boundaries are visible in every listing.
