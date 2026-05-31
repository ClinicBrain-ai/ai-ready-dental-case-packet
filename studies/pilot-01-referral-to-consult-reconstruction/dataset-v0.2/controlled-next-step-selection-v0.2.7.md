# Dataset v0.2.7 Controlled Next-Step Candidate Selection

Decision status: `selected for planning only`

Decision date: May 31, 2026

Decision basis: Dataset v0.2.6 post-coding human review decision, which opened the gate for exactly 2 additional cases only.

## Scope

This file selects exactly 2 additional candidates for the next controlled Dataset v0.2 workflow step.

This is a candidate-selection and planning artifact only. It does not create abstractions, does not perform coding, does not copy source case text, does not add patient-identifying information, and does not create clinical guidance.

## Selected Candidates

| Next-step ID | Candidate ID | Specialty | Source reference | Expected transformation focus | Why selected | Required caution |
| --- | --- | --- | --- | --- | --- | --- |
| NEXT-001 | CAND-010 | Orthodontics | Diagnosis and management of root resorption by erupting canines using cone-beam computed tomography and fixed palatal appliance: a case report. PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC3014963/ | compression, translation, new cognition, treatment-intent preservation | Adds a dental/orthodontic case that is adjacent to the original dental origins but different from the endo-perio dry-run case. It tests whether imaging-informed downstream planning can be abstracted without reproducing image details or appliance-specific phrasing. | Avoid copied imaging descriptions, appliance details, figure language, and prescriptive treatment language. |
| NEXT-002 | CAND-016 | Gastroenterology | Complexities of Occult and Obscure Gastrointestinal Bleeding: A Case Report. PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12937901/ | compression, new cognition, missing cognition, mechanism substitution | Adds a general medicine specialty case with a complex uncertainty-to-workup transition. It tests whether the workflow can handle multi-step specialist reasoning without turning the abstraction into clinical guidance. | Abstract only the high-level uncertainty-to-workup transition; do not copy chronology, workup sequence language, or source narrative. |

## Why These Two Were Selected

These candidates were selected because they provide a controlled expansion from the first dry run:

- one dental-domain case and one non-dental general medicine case;
- both were already included in the reviewed v0.2.1 shortlist;
- both have high methodological value with manageable medium privacy and copyright risk;
- neither requires opening the full remaining candidate batch;
- both can be tested using the existing source-distance, privacy, copyright, and non-guidance safeguards.

## Why Other Candidates Remain On Hold

The following candidates remain on hold:

- `CAND-001`
- `CAND-003`
- `CAND-005`
- `CAND-008`
- `CAND-009`
- `CAND-018`

They are not rejected. They remain eligible for later consideration, but the v0.2.6 gate authorized only 2 additional cases, not the full remaining batch.

## Candidates Already Used in the Dry Run

The following candidates were already used in the v0.2.2 / v0.2.5 dry-run workflow:

- `CAND-006`
- `CAND-012`

They should not be reselected for the v0.2.7 controlled next step.

## Explicit Non-Authorization

This decision does not authorize:

- creating abstractions for `CAND-010` or `CAND-016`;
- coding `CAND-010` or `CAND-016`;
- opening the remaining 8 candidates as a full batch;
- modifying `ABS-001.md` or `ABS-002.md`;
- modifying existing v0.2.5 coding outputs;
- copying or quoting source case text;
- scraping source websites;
- adding patient-identifying information;
- creating clinical guidance;
- starting Research Note 002.

## Required Next Gate

Before abstraction begins, the next step should create a limited abstraction plan for `CAND-010` and `CAND-016` only.

That plan should restate:

- source-distance requirements;
- privacy and identifiability safeguards;
- copyright and paraphrase boundaries;
- non-guidance language requirements;
- human review requirement before any coding.

Research Note 002 remains prohibited until the controlled next step is completed, reviewed, and explicitly authorized by a later decision record.

## Companion Audit Files

- [Candidate comparison v0.2.7](candidate-comparison-v0.2.7.md)
- [Safeguards checklist v0.2.7](safeguards-checklist-v0.2.7.md)
- [Pre-abstraction gate v0.2.7](pre-abstraction-gate-v0.2.7.md)
- [GitHub issue draft v0.2.7](github-issue-draft-v0.2.7.md)
