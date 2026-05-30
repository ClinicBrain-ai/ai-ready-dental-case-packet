# ADR 0001: Specification-First Dental Context Infrastructure

## Status

Accepted

CCTL-era note: this decision records the original DCS infrastructure strategy. It is retained as project history and as guidance for the DCS representation experiment, not as the current repository-wide research identity.

## Context

Dental AI systems need portable clinical context, durable agent contracts,
shared evidence semantics, and language-independent interoperability.
Optimizing for a single runtime or MVP library would make the ecosystem
dependent on implementation choices instead of shared clinical and operational
semantics.

## Decision

DCS will be developed as a specification-first standard. The canonical source of
truth is the Dental Context Specification and its machine-readable registries.
Language implementations, SDKs, service APIs, and vendor adapters are
non-normative downstream artifacts.

## Consequences

- Python, TypeScript, Rust, Go, and future implementation languages have equal
  standing because none of them defines the standard.
- Breaking changes are governed by specification versioning, not package
  release convenience.
- Clinical ontology identifiers are stable and must not be renamed casually.
- Examples, SDKs, validators, APIs, and agent adapters are downstream of the
  spec.
