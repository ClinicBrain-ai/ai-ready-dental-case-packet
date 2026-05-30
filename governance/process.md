# DCS Governance Process

Status: Foundation Draft

CCTL-era note: this file governs the historical and experimental DCS specification track. It does not define the overall mission of the repository. CCTL now treats DCS as a candidate cognitive provenance representation layer.

## Purpose

DCS governance protects semantic stability, clinical safety, privacy, and
implementation neutrality for DCS artifacts that remain in the repository.

## Principles

- The specification defines semantics; implementations demonstrate feasibility.
- Clinical meaning is reviewed by qualified dental domain reviewers.
- Backward compatibility is a release requirement, not an implementation detail.
- Extensions are encouraged when they preserve core interoperability.
- No vendor, model provider, runtime, language, API, or SDK defines DCS behavior
  by precedent alone.

## Roles

- Maintainers manage process, releases, registries, and issue disposition.
- Clinical reviewers assess dental correctness, patient safety, and risk.
- Implementer reviewers assess feasibility across independent implementations.
- Security and privacy reviewers assess PHI, custody, misuse, and auditability.
- Terminology stewards manage ontology identifiers and external bindings.

## Proposal Lifecycle

Every normative change MUST pass through:

1. Problem statement.
2. Proposed normative text.
3. Compatibility analysis.
4. Safety and clinical risk analysis.
5. Security and privacy analysis.
6. Implementation impact analysis.
7. Public review period.
8. Disposition.
9. Release assignment.

## Change Classes

- Erratum: correction that does not change conformance behavior.
- Clarification: improved wording that preserves semantics.
- Compatible addition: optional or additive feature preserving compatibility.
- Deprecation: retained feature marked for future removal or replacement.
- Breaking change: incompatible semantic or validation change requiring a major
  version.

## Release Requirements

Stable releases MUST include:

- normative specification text;
- machine-readable registries;
- compatibility classification;
- conformance criteria;
- migration notes for changed artifacts;
- extension registry updates when applicable.

## Appeals

Rejected proposals MAY be appealed when new clinical, safety, compatibility, or
implementation evidence is provided. Appeals MUST identify the disputed decision
and the new evidence.
