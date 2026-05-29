# ai-ready-dental-case-packet

`ai-ready-dental-case-packet` is an open-source MVP CLI for turning local dental records into a de-identified, structured Dental Case Packet that can be used by LLM and AI workflow tools.

It does not diagnose, does not recommend treatment, and does not replace dentist review. All AI-facing output is marked for clinical review only.

## Why Dental Teams Need This

Dental cases often arrive as scattered CBCT DICOM studies, X-rays, intraoral scans, photos, clinical notes, and treatment plans. AI workflows work better when those records are organized into predictable references, summaries, file indexes, and safety disclaimers. This project creates that packet while avoiding direct inclusion of large imaging files in the JSON output.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## CLI Usage

Build a packet:

```bash
python -m dental_packet build --input ./project-input --output ./case_packet_output
```

Validate a generated packet:

```bash
python -m dental_packet validate --input ./case_packet_output/case_packet.json
```

## Input Structure

```text
project-input/
  patient_info.json
  chief_complaint.txt
  clinical_notes.txt
  treatment_plan.txt
  cbct/
    *.dcm
  xray/
    *.dcm or *.jpg or *.png
  intraoral_scan/
    *.stl or *.ply or *.obj
  photos/
    *.jpg or *.png
```

## Output Structure

```text
case_packet_output/
  case_packet.json
  case_packet.md
  manifest.json
  files_index.json
  deidentified/
  thumbnails/
  logs/
```

## Supported Formats

- CBCT and X-ray DICOM: `.dcm`
- X-ray images and photos: `.jpg`, `.jpeg`, `.png`
- Intraoral scans: `.stl`, `.ply`, `.obj`
- Narrative records: `.txt`
- Patient demographic input: `patient_info.json`

## Privacy And Safety

The MVP uses allowlist-based de-identification. `patient_info.json` only retains `age` and `sex`. Text files are copied into `deidentified/` with common emails, phone numbers, and dates redacted. DICOM metadata output only includes a narrow non-sensitive allowlist:

- `Modality`
- `StudyDate`
- `SeriesDescription`
- `Manufacturer`
- `SliceThickness`
- `PixelSpacing`
- `Rows`
- `Columns`

If PHI-like DICOM fields such as `PatientName`, `PatientID`, `PatientBirthDate`, `PatientAddress`, or institution fields are detected, the pipeline logs the field name but never exports the original value.

## Non-Medical Diagnosis Statement

This project is for data organization, de-identification, format conversion, indexing, summarization, and structuring. It is not for automatic diagnosis and does not generate treatment advice. All packet content and AI outputs are for clinical review only and require dentist review.

## Development

```bash
ruff check .
pytest
```

## Roadmap

1. DICOM viewer integration
2. CBCT anatomical labeling
3. Treatment plan diff
4. PMS integration
5. OpenAI API optional summarization
6. Web upload portal
7. Taiwan dental workflow localization

