# Artifact Schema

This schema defines the minimum information needed to study cognition transfer between a referral letter and a specialist consultation note. It can be applied to public cases, educational cases, simulated cases, or future de-identified institutional records.

## Referral Letter Artifact

The referral letter is the source artifact. It represents the referring clinician's documented concern and request for specialist input.

Fields:

- Referral reason: the stated reason for referral or consultation.
- Suspected diagnosis: the referring clinician's working diagnosis, concern, or differential.
- Uncertainty statements: explicit markers of uncertainty, doubt, probability, ambiguity, or unresolved questions.
- Requested consultation: the specific question, service, opinion, procedure, or decision requested from the specialist.
- Contextual details: relevant history, findings, patient constraints, prior treatment, imaging, labs, or social context included in the referral.
- Timeline: relevant sequence of symptoms, findings, prior care, referral timing, and expected urgency.

## Specialist Consultation Artifact

The specialist consultation note is the downstream artifact. It represents a later interpretation that may preserve, transform, expand, or replace the referral cognition.

Fields:

- Final assessment: the specialist's concluding assessment or primary clinical interpretation.
- Differential diagnosis: alternative diagnoses, competing explanations, or ruled-out possibilities.
- Treatment recommendation: recommended intervention, plan, monitoring, referral, or no-treatment decision.
- Uncertainty statements: explicit markers of uncertainty, conditionality, probability, or need for further evidence.
- Rationale: reasons, mechanisms, evidence, or clinical logic supporting the assessment and plan.
- Follow-up plan: next steps, monitoring, return criteria, additional tests, handoff instructions, or patient-facing actions.

## Optional Metadata

- Specialty or service line.
- Time interval between referral and consultation.
- Source type: public case, educational case, simulated case, or de-identified institutional record.
- AI involvement: none, AI-generated summary, AI triage, AI recommendation, or unknown.
- Artifact completeness: complete, excerpted, synthetic, or reconstructed from narrative.
