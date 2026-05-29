from __future__ import annotations

import hashlib
from pathlib import Path

from dental_packet.schemas import FileManifestItem

ROLE_BY_DIR = {
    "cbct": "cbct",
    "xray": "xray",
    "intraoral_scan": "intraoral_scan",
    "photos": "photos",
}

TEXT_ROLES = {
    "patient_info.json": "patient_info",
    "chief_complaint.txt": "chief_complaint",
    "clinical_notes.txt": "clinical_notes",
    "treatment_plan.txt": "treatment_plan",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def infer_role(path: Path, input_root: Path) -> str:
    relative = path.relative_to(input_root)
    if len(relative.parts) == 1:
        return TEXT_ROLES.get(relative.name, "other")
    return ROLE_BY_DIR.get(relative.parts[0], "other")


def infer_file_type(path: Path) -> str:
    extension = path.suffix.lower()
    if extension == ".dcm":
        return "dicom"
    if extension in {".jpg", ".jpeg", ".png"}:
        return "image"
    if extension in {".stl", ".ply", ".obj"}:
        return "mesh"
    if extension == ".json":
        return "json"
    if extension == ".txt":
        return "text"
    return "unknown"


def build_file_index(input_root: Path) -> list[FileManifestItem]:
    if not input_root.exists():
        return []

    items: list[FileManifestItem] = []
    for path in sorted(p for p in input_root.rglob("*") if p.is_file()):
        items.append(
            FileManifestItem(
                file_type=infer_file_type(path),
                path=path.relative_to(input_root).as_posix(),
                sha256=sha256_file(path),
                size_bytes=path.stat().st_size,
                extension=path.suffix.lower().lstrip("."),
                role=infer_role(path, input_root),
            )
        )
    return items

