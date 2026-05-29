# Contributing

Thank you for helping build AI-native dental data infrastructure.

This project is not a dental AI application. Contributions should strengthen the open standard and tooling for transforming dental records into de-identified, AI-ready context.

## Contribution Principles

- Do not add diagnosis features.
- Do not add treatment recommendation features.
- Do not claim clinical accuracy.
- Keep all AI outputs framed as for clinical review only.
- Prefer privacy-preserving defaults.
- Prefer deterministic transformations before LLM calls.
- Keep LLM connectors optional.

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check .
pytest
```

## Pull Request Checklist

- Tests pass.
- `ruff check .` passes.
- New packet fields are documented in `docs/packet-spec.md`.
- PHI handling is explicit.
- No sample PHI is committed.
- No clinical diagnosis or treatment recommendation is introduced.
- User-facing AI text includes "for clinical review only" or equivalent language.

## Architecture Direction

Target contributions should fit one of these layers:

1. Data ingestion
2. Normalization
3. De-identification
4. Dental context building
5. AI-ready packet serialization
6. Optional LLM connectors
7. Future agent and review workflows

## Licensing Strategy

The repository currently uses MIT.

### MIT

Pros:

- Very low friction.
- Easy for clinics, vendors, and researchers to adopt.
- Familiar to Python infrastructure users.

Cons:

- No explicit patent grant.
- Does not require downstream changes to remain open.

### Apache-2.0

Pros:

- Explicit patent grant.
- Strong fit for infrastructure standards.
- Enterprise-friendly.

Cons:

- Slightly more legal overhead than MIT.

### AGPL

Pros:

- Maximizes openness for networked services.
- Prevents closed SaaS forks from avoiding contribution obligations.

Cons:

- High adoption friction for clinics, startups, and vendors.
- Often avoided by enterprise users.

## Recommendation

Use **Apache-2.0** for the long-term infrastructure project because it gives a clear patent grant while remaining broadly enterprise-friendly. MIT is acceptable for the current MVP, but Apache-2.0 is the recommended license before a v1.0 standardization push.

