from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import pydicom
from pydicom.errors import InvalidDicomError

ALLOWED_DICOM_FIELDS = {
    "Modality",
    "StudyDate",
    "SeriesDescription",
    "Manufacturer",
    "SliceThickness",
    "PixelSpacing",
    "Rows",
    "Columns",
}

PHI_DICOM_FIELDS = {
    "PatientName",
    "PatientID",
    "PatientBirthDate",
    "PatientAddress",
    "InstitutionName",
    "InstitutionAddress",
    "ReferringPhysicianName",
    "OperatorsName",
    "AccessionNumber",
}


def _safe_value(value: Any) -> Any:
    if isinstance(value, (str, int, float)):
        return value
    if isinstance(value, bytes):
        return "[BYTES]"
    if isinstance(value, list | tuple):
        return [_safe_value(item) for item in value]
    return str(value)


def scan_dicom_dir(path: Path, role: str) -> tuple[dict[str, Any], list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    file_records: list[dict[str, Any]] = []
    aggregate: dict[str, Counter[str]] = defaultdict(Counter)
    series_uids: set[str] = set()

    if not path.exists():
        return {"available": False, "series_count": 0, "dicom_metadata_summary": {}}, [], warnings

    dicom_paths = sorted(path.rglob("*.dcm"))
    for dicom_path in dicom_paths:
        relative = (
            dicom_path.name
            if path == dicom_path.parent
            else dicom_path.relative_to(path).as_posix()
        )
        try:
            dataset = pydicom.dcmread(dicom_path, stop_before_pixels=True, force=True)
        except (InvalidDicomError, OSError) as exc:
            warnings.append(f"Failed to parse DICOM {role}/{relative}: {exc.__class__.__name__}")
            continue

        metadata: dict[str, Any] = {}
        for field in sorted(ALLOWED_DICOM_FIELDS):
            if hasattr(dataset, field):
                value = _safe_value(getattr(dataset, field))
                metadata[field] = value
                aggregate[field][str(value)] += 1

        for field in sorted(PHI_DICOM_FIELDS):
            if hasattr(dataset, field):
                warnings.append(
                    f"PHI DICOM field detected and omitted in {role}/{relative}: {field}"
                )

        if hasattr(dataset, "SeriesInstanceUID"):
            series_uids.add(str(dataset.SeriesInstanceUID))

        file_records.append({"path": f"{role}/{relative}", "metadata": metadata})

    summary = {
        field: {"values": sorted(counter), "count": sum(counter.values())}
        for field, counter in aggregate.items()
    }
    return (
        {
            "available": bool(file_records),
            "series_count": len(series_uids) or (1 if file_records else 0),
            "dicom_metadata_summary": summary,
        },
        file_records,
        warnings,
    )
