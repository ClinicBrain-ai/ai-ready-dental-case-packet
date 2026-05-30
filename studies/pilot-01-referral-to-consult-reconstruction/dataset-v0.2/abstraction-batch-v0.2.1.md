# Abstraction Batch v0.2.1

This file defines the first limited abstraction batch for Dataset v0.2.1. It does not contain case abstractions, referral letters, consultation notes, or copied source text.

| Batch ID | Candidate ID | Specialty | Initial artifact target | Downstream artifact target | Expected reconstruction challenge | Expected transformation categories | Abstraction risk level | Required safeguard | Proceed / hold decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BATCH-001 | CAND-001 | Oral medicine / oral pathology | Referral-like concern about persistent oral lesion | Pathology/specialist assessment and management direction | Separating initial concern from downstream pathology interpretation | reframing, diagnostic replacement, new cognition, missing cognition | medium | Generalize lesion and pathology details; no copied narrative or image descriptions. | proceed with caution |
| BATCH-002 | CAND-003 | Oral medicine / psychiatry | Symptom presentation after medication context | Multidisciplinary attribution and management direction | Preserving uncertainty while representing medication-related reframing | reframing, mechanism substitution, new cognition, missing cognition | medium | Generalize medication chronology and avoid source symptom phrasing. | proceed with caution |
| BATCH-003 | CAND-005 | Endodontics | Persistent endodontic symptoms or unresolved tooth concern | CBCT-supported specialist diagnosis | Avoiding overdependence on imaging details | reframing, diagnostic replacement, mechanism substitution, new cognition | medium | Select one source case pattern; omit figures, tables, and exact imaging descriptions. | proceed with caution |
| BATCH-004 | CAND-006 | Endodontics / periodontics | Mixed endodontic-periodontal concern | Sequential specialist assessment and treatment direction | Keeping mechanism substitution clear without reproducing treatment sequence | mechanism substitution, compression, treatment-intent preservation | medium | Preserve only the cognition-relevant diagnostic transition. | proceed with caution |
| BATCH-005 | CAND-008 | Periodontics / orthodontics | Periodontal concern with suspected occlusal contribution | Specialist occlusal/periodontal interpretation and plan | Distinguishing causal reframing from uncertainty loss | reframing, mechanism substitution, compression, new cognition | medium | Generalize measurements and technical device details. | proceed with caution |
| BATCH-006 | CAND-009 | Periodontics / orthodontics | Periodontal concern after prior orthodontic history | Periodontal diagnosis and downstream treatment direction | Handling prior-treatment context without implying blame or guidance | reframing, missing cognition, new cognition, uncertainty-loss risk | medium | Omit unnecessary prior-care chronology and exact demographic combinations. | proceed with caution |
| BATCH-007 | CAND-010 | Orthodontics | Impacted canine or root-resorption concern | CBCT-informed orthodontic management direction | Preserving treatment intent while compressing imaging reasoning | compression, translation, new cognition, treatment-intent preservation | medium | Avoid copied imaging descriptions and appliance-specific detail. | proceed with caution |
| BATCH-008 | CAND-012 | Cardiology | Chest pain or indeterminate testing concern | Specialist-directed further evaluation and assessment | Avoiding clinical-guidance tone in general medicine abstraction | compression, new cognition, uncertainty-loss risk, diagnostic replacement | medium | Use educational label and avoid prescriptive sequencing. | proceed with caution |
| BATCH-009 | CAND-016 | Gastroenterology | Anemia or occult bleeding concern | GI workup interpretation and diagnostic direction | Compressing complex workup without erasing uncertainty | compression, new cognition, missing cognition, mechanism substitution | medium | Abstract uncertainty-to-workup transition only; no copied workup narrative. | proceed with caution |
| BATCH-010 | CAND-018 | Dermatology | Pigmented lesion screening concern | Dermoscopy/pathology-informed biopsy direction | Representing biopsy-threshold cognition without image reproduction | compression, diagnostic replacement, new cognition, uncertainty preservation | medium | Do not copy dermoscopic descriptions or figure captions. | proceed with caution |

## Batch Summary

- Candidates in batch: 10
- Marked proceed: 0
- Marked proceed with caution: 10
- Held: 0
- Main shared risks: copied source narrative, image-dependent details, chronology specificity, indirect identifiability, and accidental clinical-guidance tone.
- Batch readiness: ready for limited paraphrased educational abstraction using the safeguards checklist and output template.
