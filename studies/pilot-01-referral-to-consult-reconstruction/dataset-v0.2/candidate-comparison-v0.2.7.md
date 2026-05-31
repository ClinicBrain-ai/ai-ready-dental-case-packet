# Dataset v0.2.7 Candidate Comparison

This comparison explains why `CAND-010` and `CAND-016` were selected for the next controlled step.

This file uses source metadata and previously recorded selection rationale only. It does not copy source case text, does not create abstractions, and does not perform coding.

## Comparison Table

| Candidate | Domain | Main cognitive transition | Expected value after v0.2.5 | Main risk | Why suitable now |
| --- | --- | --- | --- | --- | --- |
| `CAND-010` | Orthodontics | Imaging-informed concern to downstream specialist plan | Tests whether the workflow can handle a dental-origin imaging-to-plan case without returning to the endo-perio pattern used in `CAND-006`. | Image and appliance details could become too source-proximate or guidance-like. | Adds dental-domain continuity while requiring a different transformation pattern: compression, translation, and treatment-intent preservation. |
| `CAND-016` | Gastroenterology | Uncertain presentation to specialist workup interpretation | Tests whether the workflow can handle a more complex non-dental workup transition after the cardiology case `CAND-012`. | Workup chronology could become too detailed or clinical-guidance-like. | Adds general medicine breadth while preserving a high-value uncertainty-to-workup reconstruction challenge. |

## Why Not Open the Full Remaining Batch

The v0.2.6 decision opened the gate for 2 additional cases only. Opening the full remaining batch would exceed the recorded human review decision and would prematurely scale before testing whether the limited workflow remains source-distant and interpretable.

## Why Not Start Research Note 002

Research Note 002 remains premature because v0.2.7 has not yet produced reviewed abstractions, coding outputs, or cross-case reconciliation. A note should wait until a later decision explicitly authorizes it.

## Main Methodological Question

Can the workflow move from a two-case dry run to a four-case controlled sequence while preserving:

- source distance;
- non-identifiability;
- non-guidance framing;
- interpretable reconstruction categories;
- clear separation between abstraction, review, and coding gates.

## Planned Use

This comparison supports pre-abstraction review only. It should not be treated as approval to abstract or code the selected candidates.
