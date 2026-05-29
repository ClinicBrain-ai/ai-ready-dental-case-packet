# Dental Case Packet Specification v0.1

Status: Draft  
Scope: AI-ready dental data context for clinical review  
Clinical status: Non-diagnostic, not treatment advice

## Purpose

The Dental Case Packet is a portable JSON representation of de-identified dental case context. It is designed to be consumed by LLMs, agent frameworks, dental copilots, and clinical review systems without embedding large raw imaging files.

The packet standardizes references, metadata, summaries, missing information, review questions, and safety flags.

## Design Requirements

- Must not diagnose.
- Must not recommend treatment.
- Must not claim clinical accuracy.
- Must be suitable for dentist review.
- Must be de-identified by default.
- Must reference large source files instead of embedding them.
- Must preserve enough provenance for audit and repeatability.

## Canonical JSON Shape

```json
{
  "case_id": "case-abc123",
  "created_at": "2026-05-29T10:12:04.516035Z",
  "patient": {
    "age": 45,
    "sex": "F",
    "deidentified": true
  },
  "chief_complaint": "Patient reports discomfort around the upper right posterior area.",
  "clinical_notes_summary": "Clinical notes summary.",
  "treatment_plan_summary": "Clinician-provided treatment plan summary.",
  "imaging": {
    "cbct": {
      "available": false,
      "series_count": 0,
      "dicom_metadata_summary": {},
      "warnings": []
    },
    "xray": {
      "available": false,
      "files": []
    },
    "intraoral_scan": {
      "available": false,
      "files": [],
      "formats": []
    },
    "photos": {
      "available": false,
      "files": []
    }
  },
  "ai_ready_context": {
    "case_overview": "Structured non-diagnostic case overview.",
    "known_information": ["chief_complaint", "clinical_notes", "treatment_plan"],
    "missing_information": ["Missing CBCT DICOM records."],
    "clinical_review_questions": [
      "Please confirm that the de-identified packet accurately reflects the available records."
    ],
    "llm_prompt_context": "You are reviewing a de-identified dental case packet. Do not diagnose..."
  },
  "safety": {
    "not_for_diagnosis": true,
    "requires_dentist_review": true,
    "phi_removed": true
  }
}
```

## Field Definitions

### Root

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `case_id` | string | yes | Opaque identifier generated for the packet. Must not contain PHI. |
| `created_at` | datetime | yes | UTC timestamp when the packet was created. |
| `patient` | object | yes | Minimal de-identified demographic object. |
| `chief_complaint` | string | yes | De-identified chief complaint text. Empty string when unavailable. |
| `clinical_notes_summary` | string | yes | De-identified summary of clinical notes. |
| `treatment_plan_summary` | string | yes | De-identified summary of clinician-provided plan. |
| `imaging` | object | yes | Availability and metadata for imaging and scan records. |
| `ai_ready_context` | object | yes | LLM-ready non-diagnostic context. |
| `safety` | object | yes | Required safety flags. |

### Patient

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `age` | integer or null | yes | Age if explicitly provided and allowed by policy. |
| `sex` | string or null | yes | Sex if explicitly provided and allowed by policy. |
| `deidentified` | boolean | yes | Must be `true` for compliant packets. |

### Imaging

`imaging.cbct` summarizes CBCT DICOM availability and allowlisted metadata.

`imaging.xray.files` contains references and metadata for DICOM, JPG, or PNG radiographs.

`imaging.intraoral_scan.files` contains references, hashes, formats, and simple mesh metadata for STL, PLY, and OBJ files.

`imaging.photos.files` contains references for JPG or PNG clinical photos.

### AI-ready Context

`llm_prompt_context` must include non-diagnostic instructions equivalent to:

> You are reviewing a de-identified dental case packet. Do not diagnose. Do not provide treatment recommendations.

It may ask an LLM to:

- summarize available information
- identify missing records
- produce questions for dentist review
- reformat structured context

It must not ask an LLM to:

- diagnose
- recommend treatment
- grade clinical quality as fact
- replace dentist review

## Validation Rules

1. `patient.deidentified` must be `true`.
2. `safety.not_for_diagnosis` must be `true`.
3. `safety.requires_dentist_review` must be `true`.
4. `safety.phi_removed` must be `true`.
5. Large source files must be referenced, not embedded.
6. DICOM metadata must use an allowlist.
7. Known PHI fields must not appear in packet JSON.
8. `llm_prompt_context` must include non-diagnostic language.
9. Missing record categories should be explicitly represented.
10. Packet generation should produce a manifest with SHA-256 hashes.

## Privacy Requirements

- Use allowlists before blocklists.
- Treat filenames as potentially identifying.
- Do not export raw DICOM PHI values.
- Do not export PatientName, PatientID, BirthDate, Address, Institution, or provider names.
- Logs may include field names and warning codes but must not include raw PHI values.
- Photos and pixel data may contain burned-in identifiers and require explicit handling in future versions.
- De-identified output must be reviewed before sharing outside a clinical environment.

## Example Manifest Item

```json
{
  "file_type": "mesh",
  "path": "intraoral_scan/upper_arch.stl",
  "sha256": "7a2f...",
  "size_bytes": 1842882,
  "extension": "stl",
  "role": "intraoral_scan"
}
```

## Compatibility Policy

Until v1.0, the packet format is draft and may change. After v1.0:

- additive fields should be minor version changes
- renamed or removed fields should require a major version change
- validators should reject unknown fields only for strict-mode workflows

