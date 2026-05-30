# Referral-to-Consult Cognition Reconstruction

Positioning: initial pilot study for exploring clinical cognition transformation.

## Background

Referral workflows create a natural artifact transition. A referring clinician documents a concern, rationale, uncertainty, and request. A specialist later produces a consultation note that may preserve, reframe, expand, or replace the original cognition.

This pilot tests whether clinical cognition can be partially reconstructed from the transition between referral letters and specialist consultation notes.

## Research Question

How much clinical cognition survives between a referral letter and a specialist consultation note?

## Current Status

Dataset v0.1 has been created using 10 synthetic educational referral-consult pairs. The first coding pass has been completed, including case-level coding files, aggregate results, transformation frequencies, ground-truth comparison, and a feasibility memo.

The next step is Dataset v0.2 using messier published educational cases and ideally a second coder.

## Study Materials

- [Dataset v0.1](dataset-v0.1/)
- [Dataset v0.1 summary](dataset-v0.1/dataset-summary.md)
- [Proof-of-concept analysis plan](dataset-v0.1/proof-of-concept-analysis-plan.md)
- [Analysis v0.1](analysis-v0.1/)
- [Results table](analysis-v0.1/results-table.md)
- [Transformation frequency table](analysis-v0.1/transformation-frequency-table.md)
- [Ground-truth comparison](analysis-v0.1/ground-truth-comparison.md)
- [Feasibility memo](analysis-v0.1/feasibility-memo.md)
- [Research Note 001](../../research-notes/001-synthetic-referral-consult-reconstruction-feasibility.md)

## Artifact Pair

Primary artifact pair:

- source artifact: referral letter;
- downstream artifact: specialist consultation note.

Optional contextual metadata:

- specialty;
- time interval between referral and consult;
- reason for referral;
- presence of imaging, labs, or prior notes;
- whether AI-generated summaries were used.

## Reconstruction Method

Researchers annotate each artifact pair for:

- preserved cognition: claims, concerns, evidence, or uncertainty that remain traceable;
- transformed cognition: material reframed, narrowed, expanded, or translated by the specialist;
- missing cognition: reasoning implied by the consult but absent from the referral;
- newly introduced cognition: new diagnoses, mechanisms, risks, or recommendations;
- delegated cognition: questions explicitly assigned to the specialist or another system.

The analysis produces a reconstruction hypothesis describing what upstream cognition can reasonably be inferred from the referral and how it changed in the consultation note.

## Expected Transformations

- Diagnostic reframing from broad concern to specialist problem definition.
- Uncertainty compression when referral ambiguity becomes a specific plan.
- Mechanism substitution when the specialist explains the problem differently.
- Evidence filtering when only some upstream details remain salient.
- Responsibility reassignment from referring clinician to specialist.

## Evaluation Strategy

Evaluation should focus on partial reconstruction, not perfect recovery.

Suggested measures:

- proportion of referral claims preserved in the consult note;
- number and type of newly introduced claims;
- preservation of uncertainty markers;
- agreement between independent annotators;
- severity of diagnostic or treatment reframing;
- clarity of treatment intent across the transition.

## Risks and Limitations

- Referral letters may be too sparse to support reconstruction.
- Consultation notes may retrospectively rationalize reasoning.
- Artifact pairs may omit informal communication.
- Specialty norms may strongly shape documentation style.
- The study cannot prove what clinicians privately thought.

## Ethical Considerations

- Use de-identified artifacts or synthetic/published cases for early testing.
- Avoid evaluating individual clinician quality unless explicitly designed and approved for that purpose.
- Treat reconstruction as probabilistic and limited.
- Preserve privacy, institutional confidentiality, and patient context.

## Minimal Viable Study Design

Start with 10 to 20 de-identified or publicly available referral-consult pairs from one specialty area. Two reviewers independently annotate each pair using the reconstruction categories above. Compare reviewer agreement, common transformation patterns, and cases where cognition becomes unrecoverable.

The minimal output is a feasibility report showing whether referral-to-consult artifact pairs can support disciplined partial reconstruction of clinical cognition.
