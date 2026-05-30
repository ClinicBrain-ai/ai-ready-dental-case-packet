# Dataset v0.2 Execution Plan

Dataset v0.2 will test the reconstruction workflow on 10 educational or public cases using citation-only source tracking and paraphrased educational abstractions.

## Guardrails

- Use 10 educational or public cases.
- Use 2 coders if possible.
- Maintain a citation-only source index.
- Use paraphrased educational abstractions.
- Do not copy full case text.
- Do not include patient-identifying details.
- Do not create clinical guidance.
- Compare findings against Dataset v0.1 feasibility results.

## Milestones

1. Identify 20 candidate sources.

   Use public educational materials, published teaching cases, case reports with accessible abstracts, specialty training materials, or other lawful citation-linked sources.

2. Select 10 eligible cases.

   Apply `source-eligibility-criteria.md` and exclude cases with privacy, copyright, or artifact-structure problems.

3. Create citation-only case index.

   Use `case-index-template.md`. Record source metadata and risk notes without copying case text.

4. Create paraphrased educational abstractions.

   Use `case-abstraction-protocol.md`. Label every pair as educational abstraction, not clinical documentation.

5. Run independent coding.

   Two coders independently apply the reconstruction protocol, coding framework, compression rule, and rubric.

6. Reconcile disagreements.

   Compare transformation categories, scores, confidence labels, and compression versus uncertainty-loss calls.

7. Compare to v0.1.

   Ask whether published educational cases are messier than synthetic cases and whether rubric scores show more spread.

8. Write Research Note 002.

   Use `future-research-note-002.md` as the scaffold.

## Expected Outputs

- Candidate source list.
- Eligibility decisions.
- Citation-only case index.
- 10 paraphrased educational artifact pairs.
- Independent coder files.
- Reconciled coding summary.
- Comparison with Dataset v0.1.
- Research Note 002 draft.

## Stop Conditions

Pause Dataset v0.2 if eligible public cases cannot be abstracted without copying protected text or if source materials contain identifiable patient details that cannot be safely removed.
