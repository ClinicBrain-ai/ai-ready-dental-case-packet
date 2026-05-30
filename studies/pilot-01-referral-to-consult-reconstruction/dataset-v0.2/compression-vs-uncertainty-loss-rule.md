# Compression vs Uncertainty-Loss Rule

Dataset v0.1 showed that the most difficult coding distinction was compression versus uncertainty loss. Dataset v0.2 should use the following rule.

## Compression

Code as compression when uncertainty is narrowed or summarized, but some caveat, differential, contingency, or unresolved question remains visible.

Examples:

- A referral lists three possibilities, and the consultation favors one while still naming alternatives.
- A downstream plan recommends biopsy but states that benign causes remain possible.
- A specialist recommends testing because a diagnosis is suspected but not confirmed.
- A final plan is more actionable than the referral, but the note preserves why uncertainty remains.

Coding rule:

Use compression when the downstream artifact makes uncertainty more compact or action-oriented without erasing it.

## Uncertainty Loss

Code as uncertainty loss when uncertainty disappears, is converted into certainty, or alternative diagnoses and caveats are removed.

Examples:

- A referral says infection versus noninfectious inflammation, but the downstream note states infection as fact without rationale.
- A tentative differential becomes a single diagnosis without acknowledging unresolved evidence.
- A consultation omits prior caveats that are necessary for understanding risk.
- An AI summary removes uncertainty language and presents the recommendation as settled.

Coding rule:

Use uncertainty loss when the downstream artifact makes the case appear more certain than the source artifact supports.

## Borderline Case

If the downstream artifact narrows uncertainty and preserves only a weak caveat, code as:

> compression with uncertainty-loss risk.

Examples:

- A plan says a diagnosis is \"likely\" but removes the original alternative diagnoses.
- A specialist recommends treatment while briefly noting that confirmation is pending.
- A summary preserves uncertainty in one sentence but the rest of the artifact reads as settled.

## Documentation Requirement

For every compression or uncertainty-loss code, record:

- source uncertainty;
- downstream uncertainty language;
- what was narrowed, omitted, or converted;
- whether the coding decision was clear or borderline.
