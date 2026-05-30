# Second-Coder Workflow

Dataset v0.2 should introduce a lightweight two-reviewer coding workflow to test whether the reconstruction method produces reproducible outputs.

## Independent Coding

Two coders independently review each abstraction using:

- `../coding-framework.md`
- `../evaluation-rubric.md`
- `../reconstruction-protocol.md`
- `compression-vs-uncertainty-loss-rule.md`

Coders should not view any source-selection notes that reveal intended transformation categories during initial coding.

## No Ground-Truth Viewing During Initial Coding

Dataset v0.2 may not have true ground truth. If a case has source notes, author teaching points, or abstraction notes, coders should not view them during initial reconstruction.

## Coding Categories

Coders apply the existing transformation categories:

- preservation;
- compression;
- delegation;
- translation;
- reframing;
- diagnostic replacement;
- mechanism substitution;
- uncertainty loss;
- new cognition;
- missing cognition.

## Rubric Scoring

Each coder scores the rubric dimensions from 0-4:

- reasoning preservation;
- uncertainty preservation;
- treatment intent preservation;
- cognitive drift;
- introduced reasoning.

Coders should also assign a reconstruction confidence label:

- high;
- moderate;
- low;
- unrecoverable.

## Disagreement Reconciliation

After independent coding, coders compare:

- transformation categories;
- rubric scores;
- reconstruction confidence;
- narrative reconstruction hypotheses;
- compression versus uncertainty-loss decisions.

Disagreements should be discussed and documented. The reconciled code should be recorded separately from original coder files.

## Compression vs Uncertainty-Loss Adjudication

Use `compression-vs-uncertainty-loss-rule.md` during reconciliation. If disagreement remains, code the case as compression with uncertainty-loss risk and document why.

## Documentation of Unresolved Disagreements

Unresolved disagreement is a methodological finding. Record:

- disputed code or score;
- coder A rationale;
- coder B rationale;
- why reconciliation failed;
- whether the protocol needs refinement.

## Lightweight Inter-Rater Reliability Plan

- Percent agreement for transformation categories.
- Score difference distribution for rubric dimensions.
- Qualitative disagreement memo.
- Optional Cohen's kappa only if category counts are sufficient and categories are not too sparse.

Dataset v0.2 should prioritize learning where the method breaks before treating reliability estimates as stable.
