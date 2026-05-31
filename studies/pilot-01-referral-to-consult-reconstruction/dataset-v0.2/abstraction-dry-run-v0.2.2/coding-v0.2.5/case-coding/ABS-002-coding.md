# ABS-002 Reconstruction Coding

## Scope

- Abstraction ID: ABS-002
- Source Candidate ID: CAND-012
- Specialty: Cardiology
- Source artifacts used: `ABS-002.md` only
- Coding status: limited dry-run coding complete

This coding is based only on the paraphrased educational abstraction. It is not clinical validation, not clinical guidance, and should not be used for patient care.

## Reconstructed Source Cognition

The referral-like artifact appears to encode unresolved concern about chest discomfort under incomplete evidence. The upstream cognitive frame is not a confident diagnosis but a request for interpretation of residual cardiac risk. The referring artifact delegates risk interpretation and uncertainty handling to cardiology.

## Preserved Cognition

- Chest discomfort remains the central concern.
- Uncertainty about cardiac versus non-cardiac explanation remains visible.
- The need for specialist interpretation is preserved.
- The downstream artifact preserves the idea that initial information is not fully settling.

## Transformed Cognition

- Broad uncertainty becomes a more focused downstream risk frame.
- The downstream artifact compresses the referral uncertainty into concern about whether initial findings should be treated as reassuring.
- The consultation-like artifact shifts from open-ended uncertainty to prioritized unresolved cardiac risk.

## Missing Cognition

- The abstraction omits the clinical basis for the initial assessment.
- Specific tests, values, chronology, and source narrative are intentionally absent.
- The evidence that would justify prioritizing cardiac risk downstream is not fully visible.

## Newly Introduced Cognition

- The downstream artifact introduces a risk-framing interpretation.
- It adds the idea that initial findings should be interpreted in context rather than treated as fully reassuring.
- It introduces downstream action as a cognitive marker of compressed uncertainty, without prescribing clinical care.

## Drift Characterization

Main drift: compression with uncertainty-loss risk.

The downstream artifact narrows broad uncertainty into a focused risk interpretation. Uncertainty is not erased because cardiac and non-cardiac possibilities remain visible, but the downstream frame prioritizes cardiac risk more strongly than the referral-like artifact.

## Coding Categories Applied

- Preservation: chest discomfort and unresolved uncertainty remain traceable.
- Delegation: the referral asks for specialist interpretation of residual risk.
- Compression: broad uncertainty is narrowed into a focused downstream risk frame.
- New cognition: contextual interpretation of initial findings appears downstream.
- Missing cognition: detailed evidence and chronology are absent.
- Uncertainty loss risk: downstream prioritization could reduce visibility of alternatives if coded too strongly.
- Diagnostic reframing: the downstream frame shifts from uncertain presentation to risk-focused interpretation.

## Rubric Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Reasoning preservation | 3 | The uncertainty-to-risk-frame reasoning remains traceable, but supporting clinical evidence is generalized. |
| Uncertainty preservation | 3 | Uncertainty is preserved, though alternatives are compressed. |
| Treatment intent preservation | 2 | Downstream action is represented only as a cognitive marker, so treatment intent is intentionally thin. |
| Cognitive drift | 3 | Drift is moderate and mostly explained by risk-framing cognition. |
| Introduced reasoning | 3 | New risk interpretation is identifiable, but evidentiary support is intentionally abstracted. |

Average score: 2.8 / 4

## Reconstruction Confidence

Moderate.

Confidence is strongest for uncertainty compression and delegation. Confidence is lower for treatment intent and the evidentiary basis of downstream risk prioritization.

## Notes for Adjudication

This abstraction is useful for testing the boundary between compression and uncertainty loss. It may be too generalized for fine-grained treatment-intent scoring.
