from __future__ import annotations

from pathlib import Path
from typing import Any

import trimesh

from dental_packet.file_indexer import sha256_file

SCAN_EXTENSIONS = {".stl", ".ply", ".obj"}


def parse_intraoral_scans(input_root: Path) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    scan_root = input_root / "intraoral_scan"
    warnings: list[str] = []
    records: list[dict[str, Any]] = []
    formats: set[str] = set()

    if not scan_root.exists():
        return records, [], warnings

    for path in sorted(
        p for p in scan_root.rglob("*") if p.is_file() and p.suffix.lower() in SCAN_EXTENSIONS
    ):
        extension = path.suffix.lower().lstrip(".")
        formats.add(extension)
        relative = path.relative_to(input_root).as_posix()
        record: dict[str, Any] = {
            "path": relative,
            "format": extension,
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        try:
            mesh = trimesh.load(path, force="mesh", process=False)
            record["mesh_metadata"] = {
                "vertices": int(len(getattr(mesh, "vertices", []))),
                "faces": int(len(getattr(mesh, "faces", []))),
                "is_empty": bool(getattr(mesh, "is_empty", True)),
            }
        except Exception as exc:  # noqa: BLE001 - parser should never break the pipeline.
            warning = f"Failed to parse intraoral scan {relative}: {exc.__class__.__name__}"
            warnings.append(warning)
            record["warning"] = warning
        records.append(record)

    return records, sorted(formats), warnings
