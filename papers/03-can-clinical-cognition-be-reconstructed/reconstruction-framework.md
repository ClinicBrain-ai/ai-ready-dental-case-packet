# Reconstruction Framework

## Purpose

This framework defines a cautious method for reconstructing clinical cognition from downstream artifacts. It is designed for partial reconstruction, not perfect recovery of the original reasoning event.

## Inputs

### Source Artifact

The upstream artifact that carries an earlier representation of clinical cognition.

Examples:

- referral letter;
- primary assessment;
- human assessment;
- initial clinical documentation;
- pre-AI clinician note.

### Downstream Artifact

The later artifact that carries a transformed, compressed, delegated, or expanded representation of cognition.

Examples:

- specialist consultation note;
- final treatment plan;
- AI interpretation;
- AI summary;
- longitudinal follow-up note;
- patient-facing explanation.

### Contextual Metadata

Information needed to interpret the artifact transition.

Examples:

- time interval between artifacts;
- clinical role or specialty;
- workflow stage;
- intended audience;
- known AI involvement;
- institutional template or protocol;
- available new information;
- patient constraints or preferences.

## Inference Layers

### Preserved Cognition

Elements of cognition that remain traceable across artifacts.

Examples:

- same diagnostic concern;
- same causal mechanism;
- same uncertainty marker;
- same treatment intent;
- same evidence priority.

### Transformed Cognition

Elements that remain related but change form, emphasis, scope, or meaning.

Examples:

- tentative concern becomes operational plan;
- broad differential becomes narrow working diagnosis;
- specialist reframes the original problem;
- uncertainty becomes a ranked recommendation.

### Delegated Cognition

Cognitive work assigned to another actor, AI system, workflow, or downstream artifact.

Examples:

- AI summarizes longitudinal history;
- specialist resolves diagnostic uncertainty;
- protocol determines next step;
- patient-facing tool translates clinician reasoning.

### Missing Cognition

Reasoning that appears necessary for understanding the transition but is absent or unrecoverable.

Examples:

- no documented rationale for referral;
- unexplained treatment selection;
- missing uncertainty statement;
- undocumented assumption about patient preference;
- absent source for AI-generated claim.

### Newly Introduced Cognition

Claims, interpretations, recommendations, or uncertainties that appear downstream without a clear upstream source.

Examples:

- new diagnosis in consultation note;
- AI-generated risk statement;
- new causal explanation;
- added treatment priority;
- new patient-facing simplification.

## Outputs

### Reconstruction Hypothesis

A structured account of the prior cognition most likely represented by the artifact transition.

The hypothesis should identify:

- inferred clinical concern;
- inferred rationale;
- inferred uncertainty;
- inferred treatment intent;
- evidence supporting the inference;
- alternative plausible reconstructions.

### Uncertainty Assessment

An explicit statement of confidence and limits.

The assessment should identify:

- high-confidence inferences;
- low-confidence inferences;
- missing evidence;
- ambiguity between competing reconstructions;
- points where cognition is unrecoverable.

### Drift Characterization

A description of how cognition changed across the transition.

Possible drift types:

- diagnostic reframing;
- recommendation drift;
- uncertainty compression;
- evidence omission;
- mechanism substitution;
- responsibility shift;
- patient-facing simplification;
- AI-mediated transformation.

## Suggested Artifact Pairs

- Referral Letter <-> Specialist Consultation Note.
- Primary Assessment <-> Final Treatment Plan.
- Clinical Documentation <-> AI Interpretation.
- Human Assessment <-> AI Summary.

## Methodological Guardrails

- Do not claim full recovery of original cognition.
- Preserve uncertainty when multiple reconstructions are plausible.
- Distinguish upstream cognition from downstream additions.
- Treat documentation as a transformed artifact, not a neutral transcript.
- Account for workflow, institutional, and audience effects.
- Identify unrecoverable cognition explicitly.
