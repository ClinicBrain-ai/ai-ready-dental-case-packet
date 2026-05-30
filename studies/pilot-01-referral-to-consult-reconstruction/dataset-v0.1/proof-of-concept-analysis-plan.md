# Proof-of-Concept Analysis Plan

This plan describes how to code Dataset v0.1 using the existing Pilot 1 materials:

- `../coding-framework.md`
- `../evaluation-rubric.md`
- `../reconstruction-protocol.md`

Ground Truth Reasoning Notes are reserved for evaluation and should not be used during the initial reconstruction pass.

## Step 1: Blind Reconstruction Pass

For each case, read only:

- Case ID;
- Referral Letter;
- Specialist Consultation Note.

Do not read Ground Truth Reasoning Notes.

Apply `reconstruction-protocol.md`:

1. Read referral artifact.
2. Infer likely source cognition.
3. Read consultation artifact.
4. Identify preserved cognition.
5. Identify transformed cognition.
6. Identify missing cognition.
7. Identify newly introduced cognition.
8. Characterize drift.
9. Generate reconstruction hypothesis.

## Step 2: Code Transformation Types

Use `coding-framework.md` to assign one or more codes to each case:

- Preservation;
- Compression;
- Delegation;
- Translation;
- Reframing;
- Diagnostic Replacement;
- Mechanism Substitution;
- Uncertainty Loss;
- New Cognition;
- Missing Cognition.

Record a short evidence note for every assigned code.

## Step 3: Score Reconstruction Quality

Use `evaluation-rubric.md` to score each pair from 0-4 on:

- reasoning preservation;
- uncertainty preservation;
- treatment intent preservation;
- cognitive drift;
- introduced reasoning.

Lower cognitive drift scores indicate severe or unexplained drift. Higher scores indicate no major drift or well-explained drift.

## Step 4: Compare Against Ground Truth

After the blind reconstruction pass is complete, read the Ground Truth Reasoning Notes.

Compare each reconstruction hypothesis against:

- original referring clinician reasoning;
- original uncertainty;
- suspected diagnosis;
- rationale for referral.

Record whether the blind reconstruction captured the intended source cognition fully, partially, weakly, or not at all.

## Step 5: Summarize Feasibility

Produce a short feasibility memo with:

- number of cases successfully reconstructed;
- most common transformation codes;
- categories that were hard to apply;
- fields most useful for reconstruction;
- fields most often missing;
- whether ground truth comparison showed systematic over-inference or under-inference.

## Expected Outputs

- 10 completed reconstruction hypotheses.
- 10 coded transformation profiles.
- 10 rubric score sets.
- A brief comparison against ground truth notes.
- A short feasibility memo recommending changes before Dataset v0.2.

## Guardrails

- Do not treat synthetic cases as evidence of real-world frequency.
- Do not use Ground Truth notes during the initial reconstruction pass.
- Preserve uncertainty when multiple reconstructions are plausible.
- Record over-inference as a methodological risk.
