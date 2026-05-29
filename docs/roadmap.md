# Roadmap

## v0.1 Case Packet Builder

- Local CLI.
- Folder-based ingestion.
- File manifest and SHA-256 indexing.
- DICOM metadata allowlist.
- STL, PLY, OBJ mesh metadata.
- Basic de-identification.
- Markdown report.
- Pydantic validation.

## v0.2 DICOM Thumbnail Service

- Generate safe thumbnails from DICOM and image records.
- Detect and warn about burned-in annotations.
- Keep thumbnails separate from packet JSON.
- Add thumbnail provenance metadata.

## v0.3 Treatment Plan Parser

- Parse clinician-provided plans into structured sections.
- Preserve original intent without generating recommendations.
- Add treatment plan diff support for versioned plans.

## v0.4 Dental Context Builder

- Separate context construction from CLI orchestration.
- Add provenance to every generated context field.
- Add deterministic missing-information detection.
- Introduce structured warning codes.

## v0.5 FHIR Mapping

- Map packet fields to relevant FHIR resources where possible.
- Document dentistry-specific gaps in FHIR.
- Add export adapters for clinical interoperability.

## v0.6 OpenAI Connector

- Optional connector for OpenAI models.
- Non-diagnostic prompt templates.
- Redaction guardrails before request creation.
- Strict "for clinical review only" output framing.

## v0.7 Dental RAG

- Chunk clinical notes, plans, and metadata.
- Add retrieval contracts for packet sections.
- Support local vector stores.
- Avoid using RAG to generate diagnosis or treatment recommendations.

## v0.8 Dental Agent SDK

- Review workflow primitives.
- Task handoff to dentists.
- Audit trail for agent actions.
- Tool contracts for future clinical copilots.

## v1.0 AI-native Dental Infrastructure Platform

- Stable Dental Case Packet Specification.
- Versioned JSON Schema.
- Plugin ecosystem for PMS, lab, imaging, and LLM connectors.
- Privacy profiles for HIPAA, GDPR, and Taiwan workflows.
- Production-ready CLI and library APIs.

