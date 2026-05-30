# Dental Context Specification: A Minimal Claim Provenance Layer for Dental Agent Handoffs

> Historical note: This document is a legacy DCS / dental packet infrastructure artifact from the project's earlier phase. The current primary repository identity is Clinical Cognition Transformation Lab (CCTL), which studies how clinical cognition transforms in distributed human-AI healthcare systems. This file is preserved for historical and technical context, not as the current primary mission statement.

## Abstract

Dental artificial intelligence is moving from isolated model outputs toward networks of specialized agents that observe, reason, verify, communicate, and coordinate care. Existing standards and systems represent important parts of the clinical environment: DICOM represents imaging objects, FHIR represents broad healthcare resources, OpenAPI describes service interfaces, and emerging agent protocols connect agents to tools and to one another. None of these, by themselves, define the minimal dental claim provenance artifact needed to preserve semantic accountability when one agent relies on another agent's output.

The Dental Context Specification (DCS) proposes a minimal, vendor-neutral claim provenance format for dental agent handoffs. DCS is intended to make each dental claim traceable to evidence, supporting claims, contradicting claims, uncertainty, author, provenance, timestamp, and review status. It is not a transport protocol, model architecture, clinical decision engine, product interface, broad ontology, complete dental data standard, or replacement for existing healthcare standards.

## Thesis

Future dental AI systems will not be single models. They will be networks of specialized agents. These agents require a minimal claim provenance layer for semantic accountability across dental agent handoffs. DCS proposes that layer.

## 1. Motivation

### 1.1 Model-Centric Dental AI Is Insufficient

Most current dental AI systems are model-centric. A model receives an image, chart, note, or claim and returns a prediction, label, score, segmentation, or generated explanation. This can be useful, but it is insufficient as a foundation for agent-native dentistry.

Model-centric outputs often fail to preserve:

- what evidence was used;
- how observations were transformed into findings;
- which hypotheses were considered;
- what uncertainty remains;
- which contradictions were detected;
- which recommendation depends on which diagnosis;
- whether a human reviewed the result;
- whether downstream agents can safely reuse the result.

A dental ecosystem composed of many agents cannot rely on opaque outputs. It requires traceable claims that can be inspected, challenged, and carried forward.

### 1.2 Agent-Native Dentistry Requires Claim Provenance

Agent-native dentistry assumes that multiple specialized agents participate in clinical and administrative workflows. An imaging agent may identify radiographic observations. A diagnostic agent may relate observations to disease hypotheses. A treatment planning agent may propose options. A verification agent may test whether the recommendation follows from the evidence. A patient communication agent may explain reviewed decisions in patient-facing language. Referral, insurance, and follow-up agents may consume the same case context for their own purposes.

Without shared claim provenance, each agent must reinterpret raw artifacts or trust the unstructured output of previous agents. This produces reasoning decay, repeated extraction, fragile integration, and weak auditability. DCS addresses this by defining a minimal artifact that carries dental claim meaning, evidence links, uncertainty, contradictions, provenance, and review state across handoffs.

### 1.3 Clinical Artifacts Alone Are Not Enough

Free text, PDFs, raw DICOM objects, and isolated JSON exports are important but incomplete.

Free text is expressive but ambiguous. It does not reliably expose evidence chains, uncertainty, contradictions, or machine-checkable dependencies.

PDFs preserve human-readable presentation but usually collapse structured clinical meaning into a fixed document. They are poor substrates for agent reasoning and verification.

Raw DICOM is essential for imaging interoperability, but imaging objects alone do not define dental diagnoses, treatment options, longitudinal reasoning, review status, or cross-agent semantics.

Isolated JSON exports may be structured but are often vendor-specific, workflow-specific, and semantically underdefined. JSON alone is a syntax, not a dental reasoning standard.

DCS does not replace these artifacts. It preserves the claim-level provenance needed to evaluate how their clinical significance was used.

## 2. Scope

DCS defines a minimal claim provenance layer for exchange among agents and systems. It is intended to preserve semantic accountability when claims move through imaging, diagnosis, treatment planning, insurance, patient education, referral, and longitudinal follow-up workflows.

DCS is specification-first. It should be usable independent of any model, vendor, programming language, deployment environment, or transport protocol.

## 3. What DCS Solves

DCS solves the problem of exchanging traceable dental claims across independent agents without losing reasoning provenance.

Existing standards solve adjacent problems. DICOM represents imaging objects. FHIR represents broad healthcare resources. OpenAPI describes service interfaces. MCP connects agents to tools and data sources. A2A and ACP connect agents to other agents. Dental charting systems store operational clinical records.

DCS addresses the missing layer between raw clinical artifacts and agent coordination: a minimal claim provenance format for observations, findings, diagnoses, recommendations, contradictions, uncertainty, provenance, and review status.

## 4. Core Agent-to-Agent Exchange Pattern

DCS assumes that different agents may contribute different parts of a shared case context.

1. Imaging Agent
   Produces evidence references and observations derived from radiographs, intraoral images, scans, photographs, or other imaging inputs. It does not need to make final clinical decisions.

2. Diagnostic Agent
   Consumes evidence and observations. Produces findings, hypotheses, differential considerations, diagnoses, and uncertainty statements.

3. Treatment Planning Agent
   Consumes findings, diagnoses, patient context, and chart context. Produces treatment options, recommendation rationale, dependencies, alternatives, and contraindication considerations.

4. Verification Agent
   Checks whether evidence chains are complete, whether findings are supported, whether diagnoses contradict recorded observations, and whether recommendations depend on unreviewed or uncertain claims.

5. Patient Communication Agent
   Converts reviewed decisions into patient-facing explanations while preserving links to the underlying professional context.

6. Referral, Insurance, and Follow-Up Agents
   Consume the same context for specialist referral, claim support, benefit coordination, recall planning, monitoring, and longitudinal comparison without reinterpreting the entire case from scratch.

The purpose of DCS is not to force a single workflow. It is to make claims handed between agents explicit, inspectable, and semantically accountable.

## 5. Non-Normative Architecture Diagram

```text
Raw Data / Clinical Inputs
  -> TraceableDentalClaim: Observation
  -> TraceableDentalClaim: Finding
  -> TraceableDentalClaim: Diagnosis
  -> TraceableDentalClaim: Recommendation / Contradiction
  -> Agent-to-Agent Exchange
  -> Human Review
```

The diagram is illustrative. DCS does not require a specific runtime architecture.

## 6. Claim Provenance Core

### 6.1 TraceableDentalClaim

The central object of DCS is `TraceableDentalClaim`. It identifies one dental reasoning claim and the minimum provenance needed for downstream agents and reviewers to evaluate it.

The smallest normative DCS claim includes claim identity, claim type, subject, evidence references, supporting claims, contradicting claims, uncertainty, author, timestamp, provenance, review status, and a human-readable summary.

### 6.2 Claim Graph

Multiple claims form a provenance graph. An observation claim may support a finding claim. A finding claim may support a diagnosis claim. A diagnosis claim may support a recommendation claim. A contradiction claim may point to unsupported, inconsistent, or overstated claims.

This graph is the minimum structure required to preserve semantic accountability across handoffs.

### 6.3 Deferred Scope

DCS does not initially define a broad dental ontology, complete treatment planning model, full charting model, transport protocol, API, SDK, or workflow protocol. Those concerns are deferred unless needed to preserve claim provenance.

## 7. Reasoning Provenance

Reasoning provenance matters because dental recommendations affect health, cost, trust, and liability. An agent-native dental ecosystem must support review, challenge, and correction.

Every recommendation should be traceable from evidence to finding to diagnosis to treatment option to decision. This chain enables:

- clinical review by dentists and specialists;
- detection of unsupported recommendations;
- comparison of agent reasoning across versions;
- identification of contradictory evidence;
- longitudinal follow-up and revision;
- research evaluation of reasoning quality;
- defensible communication with patients, insurers, and referral partners.

DCS should treat provenance as a first-class part of context, not as an afterthought or log file.

## 8. Relationship to Other Standards and Protocols

DCS is complementary to existing standards and agent infrastructure.

MCP connects agents to tools and data sources. DCS defines the traceable dental claim artifact an agent may retrieve, update, inspect, or exchange through those tools.

A2A and ACP connect agents to other agents. DCS defines a minimal claim provenance payload that those agents can exchange.

FHIR represents broad healthcare resources. DCS can reference or map to FHIR resources where appropriate, while preserving dental claim provenance as its narrow purpose.

DICOM represents imaging objects and imaging metadata. DCS can reference DICOM studies, series, images, regions, and derived observations while preserving the claims made from that evidence.

OpenAPI describes HTTP service interfaces. DCS is not an interface description language. A service may expose DCS through an OpenAPI-described API, but OpenAPI does not define dental meaning.

Dental charting systems manage operational records. DCS can reference or encode chart context for agent exchange, but it does not replace practice management systems or clinical record systems.

## 8.1 Relationship to Normative DCS Artifacts

This white paper is non-normative. The normative and governance artifacts for DCS are maintained in the repository specification track:

- [spec/dcs.md](../spec/dcs.md): normative Dental Context Specification.
- [ontology/canonical-ontology.yaml](../ontology/canonical-ontology.yaml): canonical dental ontology registry.
- [models/reasoning-model.yaml](../models/reasoning-model.yaml): reasoning and inference model registry.
- [models/evidence-model.yaml](../models/evidence-model.yaml): evidence and provenance model registry.
- [models/agent-contract-model.yaml](../models/agent-contract-model.yaml): agent contract model registry.
- [compatibility/versioning-policy.yaml](../compatibility/versioning-policy.yaml): versioning and compatibility policy.
- [extensions/extension-policy.yaml](../extensions/extension-policy.yaml): extension mechanism and registry rules.
- [governance/process.md](../governance/process.md): standards governance process.

The white paper explains the agent-native dentistry rationale. The normative `TraceableDentalClaim` specification defines the minimal core.

## 9. Comparison Table

| System or Standard | Primary Purpose | What It Solves | What It Does Not Solve | How DCS Complements It |
| --- | --- | --- | --- | --- |
| DICOM | Medical imaging object representation and exchange | Imaging storage, metadata, study and series organization, image interoperability | Claim provenance across observations, findings, diagnoses, recommendations, and contradictions | DCS references DICOM evidence and preserves claims made from it |
| FHIR | Broad healthcare resource representation and exchange | Patient, encounter, observation, procedure, condition, and administrative interoperability | Minimal dental agent claim provenance as the central exchange artifact | DCS can reference or map to FHIR while preserving dental reasoning traceability |
| OpenAPI | Description of service interfaces | Machine-readable API contracts for HTTP services | Clinical claim semantics, provenance, contradictions, and review state | DCS can be transported through APIs described by OpenAPI |
| MCP | Agent access to tools and data sources | Tool discovery, invocation, and context access for agents | Dental claim provenance format | DCS provides a small artifact that MCP-connected tools may expose or consume |
| A2A / ACP | Agent-to-agent communication | Agent discovery, messaging, delegation, and coordination patterns | Dental-specific claim provenance payload | DCS defines the minimal dental claim artifact exchanged over agent-to-agent protocols |
| Dental charting systems | Operational dental record keeping | Charting, procedure records, treatment history, scheduling, billing integration | Cross-agent reasoning provenance and handoff accountability | DCS can reference chart context while preserving claims and their provenance |

## 10. Minimum Viable Standard

The smallest useful DCS exchange is one `TraceableDentalClaim`.

The smallest claim includes:

- claim identifier;
- claim type;
- subject;
- evidence references;
- supporting claims;
- contradicting claims;
- uncertainty;
- author;
- timestamp;
- provenance;
- review status;
- human-readable summary.

This minimum exchange is intentionally small. It is sufficient for one agent to communicate a clinically meaningful claim and for another agent to inspect the basis, uncertainty, provenance, contradictions, and review state of that claim.

## 11. Non-Goals

DCS does not:

- diagnose disease by itself;
- replace dentists;
- define transport protocols;
- replace DICOM or FHIR;
- replace MCP, A2A, ACP, OpenAPI, PMS schemas, or dental charting systems;
- mandate a specific LLM;
- mandate Python or any programming language;
- define broad dental ontology as its first normative core;
- define complete treatment planning;
- define full charting;
- define APIs or SDKs;
- guarantee clinical correctness;
- remove the need for human clinical review.

## 12. Research and Journal Contribution Framing

DCS can be positioned as an AI application and clinical informatics contribution because it reframes dental AI interoperability around traceable claims and handoff accountability rather than isolated predictions.

The contribution is a shift:

- from model-centric AI to agent-centric AI;
- from prediction output to traceable dental claims;
- from isolated dental software to interoperable dental agents;
- from raw clinical artifacts to structured claim provenance.

This framing supports research questions about reasoning decay, semantic accountability, claim provenance, cross-agent verification, clinical review workflows, handoff failure modes, and the evaluation of agent networks in dental care.

DCS is not a claim that agents should make autonomous clinical decisions. It is a proposal that, if dental agents are used, their communication should be structured, inspectable, and grounded in domain-specific context.

## 13. Governance Principles

DCS should evolve as an open specification with clear conformance language, extension rules, and clinically reviewed examples. Its governance should prioritize semantic accountability, claim provenance, vendor neutrality, and compatibility with adjacent standards.

Extensions should be explicit and discoverable. Implementations should be able to identify which parts of a DCS exchange are core, which are extensions, and which require local interpretation.

## 14. Future Work

Future work includes:

- DCS conformance levels;
- DCS test fixtures;
- reference dental claim handoff scenarios;
- mapping to FHIR and DICOM;
- human review workflows;
- journal submission version;
- public RFC process;
- governance and extension registry.

## 15. Conclusion

Dentistry needs more than better isolated models. It needs a minimal claim provenance layer that allows specialized agents to exchange dental reasoning claims without losing evidence, uncertainty, contradictions, provenance, or review status.

DCS proposes that layer. Its purpose is to make dental agent handoffs semantically accountable across models, vendors, programming languages, platforms, and protocols.
