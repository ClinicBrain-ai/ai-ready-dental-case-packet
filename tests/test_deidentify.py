from __future__ import annotations

import json

from pydicom.dataset import FileDataset

from dental_packet.deidentify import deidentify_patient_info, redact_text
from dental_packet.dicom_parser import scan_dicom_dir


def test_deidentify_patient_info_allowlist() -> None:
    data = {
        "name": "Jane Patient",
        "patient_id": "ABC123",
        "age": 42,
        "sex": "F",
        "address": "123 Street",
    }
    assert deidentify_patient_info(data) == {"age": 42, "sex": "F"}


def test_redact_text_basic_identifiers() -> None:
    text = "Email jane@example.com, phone +1 555 123 4567, date 2025-02-03."
    redacted = redact_text(text)
    assert "jane@example.com" not in redacted
    assert "555 123 4567" not in redacted
    assert "2025-02-03" not in redacted


def test_dicom_metadata_phi_not_output(tmp_path) -> None:
    dicom_dir = tmp_path / "cbct"
    dicom_dir.mkdir()
    path = dicom_dir / "image.dcm"

    dataset = FileDataset(str(path), {}, preamble=b"\0" * 128)
    dataset.PatientName = "Sensitive^Name"
    dataset.PatientID = "secret-id"
    dataset.Modality = "CT"
    dataset.SeriesDescription = "CBCT"
    dataset.Rows = 10
    dataset.Columns = 10
    dataset.save_as(path)

    summary, files, warnings = scan_dicom_dir(dicom_dir, "cbct")
    serialized = json.dumps({"summary": summary, "files": files})

    assert "Sensitive" not in serialized
    assert "secret-id" not in serialized
    assert "PatientName" in "\n".join(warnings)
    assert files[0]["metadata"]["Modality"] == "CT"
