# Dataset v0.1 Summary

Synthetic educational dataset for Pilot 1: Referral-to-Consult Reconstruction.

No cases describe real patients. No identifiable information is included.

## Case Distribution

| Case ID | Domain | Referral Pathway | Primary Scenario |
| --- | --- | --- | --- |
| P1-V01-001 | Dentistry / oral medicine | Dentist -> oral medicine | Persistent oral ulcer |
| P1-V01-002 | Oral surgery | Dentist -> oral surgery | Post-extraction pain |
| P1-V01-003 | Endodontics | Dentist -> endodontics | Persistent apical symptoms |
| P1-V01-004 | Periodontics | Dentist -> periodontics | Rapid periodontal breakdown |
| P1-V01-005 | Orthodontics | Dentist -> orthodontics | Delayed canine eruption |
| P1-V01-006 | Oral medicine | Dentist -> oral medicine | Burning mouth symptoms |
| P1-V01-007 | General medicine / cardiology | Primary care -> cardiology | Exertional chest discomfort |
| P1-V01-008 | General medicine / neurology | Primary care -> neurology | Transient neurologic episode |
| P1-V01-009 | General medicine / dermatology | Primary care -> dermatology | Changing pigmented lesion |
| P1-V01-010 | General medicine / gastroenterology | Primary care -> gastroenterology | Iron deficiency anemia |

## Specialty Distribution

- Dentistry / oral medicine: 2 cases.
- Oral surgery: 1 case.
- Endodontics: 1 case.
- Periodontics: 1 case.
- Orthodontics: 1 case.
- General medicine referral scenarios: 4 cases.

## Expected Transformation Types

- Preservation: core referral concern should remain visible in most consultation notes.
- Compression: some referral uncertainty becomes a more direct specialist assessment.
- Reframing: cases 001, 003, 004, 006, and 008 include likely diagnostic or mechanism reframing.
- Diagnostic replacement: cases 001, 003, and 006 may shift from an initial suspected diagnosis toward a different leading diagnosis.
- Mechanism substitution: cases 002, 003, 004, and 006 contain mechanism-level changes or clarification.
- Uncertainty loss: possible in cases where the specialist plan is more definitive than the referral.
- New cognition: consultation notes introduce specialist-specific rationale or additional differential diagnoses.
- Missing cognition: several referrals omit evidence details that would explain why a suspected diagnosis was considered.

## Known Uncertainty Points

- Whether persistent oral ulcer is traumatic or premalignant.
- Whether post-extraction pain represents dry socket or infection.
- Whether root-treated tooth symptoms represent endodontic failure or vertical fracture.
- Whether rapid periodontal breakdown is primarily inflammatory, mechanical, or mixed.
- Whether impacted canine creates adjacent root resorption risk.
- Whether burning mouth symptoms are mucosal, systemic, or neuropathic.
- Whether exertional chest discomfort is cardiac or non-cardiac.
- Whether transient neurologic symptoms represent TIA or mimic.
- Whether changing pigmented lesion is atypical nevus or melanoma.
- Whether iron deficiency anemia reflects dietary deficiency or occult GI blood loss.

## Intended Use

Dataset v0.1 is sufficient for a first feasibility analysis of the reconstruction protocol, coding framework, and evaluation rubric. It is not sufficient for claims about real-world frequency, specialty-level patterns, or clinical outcomes.
