# Research Note 001: Synthetic Referral-to-Consult Reconstruction Feasibility Study

## Summary

This note summarizes the first proof-of-concept coding pass for Pilot 1: Referral-to-Consult Cognition Reconstruction. The study used a synthetic educational dataset of 10 fictional referral-consult pairs to test whether the CCTL reconstruction workflow can produce interpretable outputs.

This was not a real-world clinical study. It does not establish clinical generalizability, real-world prevalence, or patient-care validity. It was a workflow feasibility test.

## Why This Study Was Run

CCTL studies how clinical cognition transforms as it moves through clinicians, documentation artifacts, AI systems, workflows, institutions, and patients. Pilot 1 asks whether cognition can be partially reconstructed from a referral letter and a specialist consultation note after the original reasoning event has disappeared.

The first step was to test whether the reconstruction protocol, coding framework, and evaluation rubric could be applied consistently enough to generate useful analytic outputs.

## Dataset

Dataset v0.1 contains 10 fictional referral-consult pairs. The cases were designed for educational proof-of-concept use and include dentistry, oral surgery, endodontics, periodontics, orthodontics, oral medicine, and general medicine referral scenarios.

Each case includes a Referral Letter, Specialist Consultation Note, and Ground Truth Reasoning Notes. The initial reconstruction pass used only the Referral Letter and Specialist Consultation Note. Ground truth notes were used later for comparison.

## Method

The coding pass used the Pilot 1 reconstruction materials:

- reconstruction protocol;
- coding framework;
- evaluation rubric;
- synthetic Dataset v0.1;
- analysis-v0.1 case-coding files.

Each case was coded for reconstructed source cognition, preserved cognition, transformed cognition, missing cognition, newly introduced cognition, drift characterization, uncertainty assessment, coding categories, and rubric scores.

## Preliminary Results

Average preservation score was 3.7 / 4.

Preservation, delegation, new cognition, and missing cognition appeared in all 10 synthetic cases. Compression appeared in 7 cases and was the most common more discriminating transformation type.

These results should be read as feasibility signals only. The dataset was intentionally synthetic and educational, so high preservation scores likely reflect the clarity of the constructed artifacts.

## Transformation Patterns

The analysis showed that the workflow can identify both continuity and change. The central referral concern was usually preserved, while specialist consultation notes introduced new reasoning, operationalized the plan, and sometimes reframed the diagnostic or causal interpretation.

Common transformations included:

- preservation of the core referral concern;
- delegation of uncertainty resolution to the specialist;
- compression of uncertainty into a more actionable assessment;
- introduction of new specialist cognition;
- missing upstream detail that limited full reconstruction.

## Key Ambiguity

The main ambiguity was distinguishing compression from uncertainty loss.

In many cases, the consultation note narrowed uncertainty but did not erase it. The coding pass therefore treated most of these cases as compression rather than full uncertainty loss. Dataset v0.2 should refine this distinction with clearer coding rules and examples.

## Feasibility Judgment

The reconstruction workflow appears feasible for a Dataset v0.2 using messier published educational cases.

The protocol produced interpretable case-level outputs, aggregate tables, transformation counts, ground-truth comparison notes, and a feasibility memo. The next test should examine whether the workflow still works when artifacts are less cleanly separated and less deliberately informative.

## Limitations

- Dataset v0.1 was synthetic and educational.
- The cases were designed to make referral and consultation structure visible.
- Scores do not estimate real-world frequencies.
- The first pass used one coding perspective rather than independent human coders.
- Real clinical documentation may be much messier, shorter, or less explicit.

## Implications for Dataset v0.2

Dataset v0.2 should use published educational cases or public case-derived materials where referral-like and consultation-like artifacts are less idealized. It should also introduce a second-coder workflow to test reproducibility.

Priority refinements include:

- clearer compression versus uncertainty-loss rules;
- explicit reconstruction confidence scoring;
- examples of over-inference and under-inference;
- messier referral artifacts;
- consultation notes with less complete rationale.

## Next Steps

1. Build Dataset v0.2 with approximately 25 cases.
2. Include published educational cases where possible.
3. Add a second independent coder.
4. Refine the coding framework based on v0.1 ambiguities.
5. Prepare a short manuscript or preprint from Pilot 1 if v0.2 remains feasible.
