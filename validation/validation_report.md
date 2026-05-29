# Clinical Validation Dataset v0.1

This validation dataset uses public-source-referenced, anonymized local fixtures.
It does not include private patient data and does not perform clinical interpretation.

## Aggregate Metrics

- Total cases: 20
- Successful packet builds: 20
- Failed packet builds: 0
- MCP success rate: 20/20
- Validation success rate: 20/20
- PHI detection results: low=20, medium=0, high=0
- Unsupported formats encountered: .gz, .pdf

## Case Results

| Case | Source dataset | Modality | Focus | Build | Validate | PHI risk | MCP | Warnings | Schema issues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cv-001 | MMDental | CBCT | implant planning | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-002 | PhysioNet multimodal dental dataset | CBCT + panoramic X-ray | implant planning | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-003 | ToothFairy | CBCT | implant planning | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-004 | Open-Full-Jaw | CBCT-derived jaw mesh | implant planning | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-005 | MMDental | CBCT | missing teeth | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-006 | PhysioNet multimodal dental dataset | panoramic X-ray | missing teeth | True | True | low | True | none | none |
| cv-007 | Teeth segmentation panoramic X-ray dataset | panoramic X-ray | missing teeth | True | True | low | True | none | none |
| cv-008 | Open-Full-Jaw | CBCT-derived jaw mesh | missing teeth | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-009 | PhysioNet multimodal dental dataset | CBCT + panoramic X-ray | orthodontics | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-010 | ToothFairy | CBCT | orthodontics | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-011 | Open-Full-Jaw | CBCT-derived full jaw model | orthodontics | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-012 | MMDental | CBCT + records | orthodontics | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-013 | MMDental | CBCT + records | endodontics | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-014 | PhysioNet multimodal dental dataset | periapical X-ray | endodontics | True | True | low | True | none | none |
| cv-015 | ToothFairy | CBCT | endodontics | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-016 | CTooth+ | CBCT | endodontics | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-017 | Open-Full-Jaw | CBCT-derived full jaw model | wisdom teeth | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-018 | PhysioNet multimodal dental dataset | panoramic X-ray | wisdom teeth | True | True | low | True | none | none |
| cv-019 | ToothFairy | CBCT | full jaw anatomy | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |
| cv-020 | CTooth+ | CBCT | full jaw anatomy | True | True | low | True | DICOM copied by reference only; metadata PHI is not exported: cbct/slice_0001.dcm | none |

## Source Datasets

- MMDental: https://www.nature.com/articles/s41597-025-05398-7 - Open-access multimodal dental dataset with CBCT images and expert records.
- PhysioNet multimodal dental dataset: https://physionet.org/content/multimodal-dental-dataset/ - Public PhysioNet dataset with CBCT, panoramic X-ray, and periapical X-ray records.
- ToothFairy: https://toothfairy3.grand-challenge.org/dataset/ - Public CBCT benchmark family for maxillofacial structure segmentation.
- CTooth+: https://www.kaggle.com/datasets/weiweicui/ctooth-dataset - Open-access CBCT tooth volume segmentation dataset.
- Open-Full-Jaw: https://arxiv.org/abs/2209.07576 - Open-access CBCT-derived human jaw model dataset and pipeline.
- Teeth segmentation panoramic X-ray dataset: https://www.kaggle.com/datasets/humansintheloop/teeth-segmentation-on-dental-x-ray-images - Open panoramic dental X-ray segmentation dataset derived from public radiographs.
