from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Patient(BaseModel):
    age: int | None = None
    sex: str | None = None
    deidentified: bool = True


class CbctImaging(BaseModel):
    available: bool = False
    series_count: int = 0
    dicom_metadata_summary: dict[str, Any] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)


class XrayImaging(BaseModel):
    available: bool = False
    files: list[dict[str, Any]] = Field(default_factory=list)


class IntraoralScanImaging(BaseModel):
    available: bool = False
    files: list[dict[str, Any]] = Field(default_factory=list)
    formats: list[str] = Field(default_factory=list)


class PhotosImaging(BaseModel):
    available: bool = False
    files: list[dict[str, Any]] = Field(default_factory=list)


class Imaging(BaseModel):
    cbct: CbctImaging = Field(default_factory=CbctImaging)
    xray: XrayImaging = Field(default_factory=XrayImaging)
    intraoral_scan: IntraoralScanImaging = Field(default_factory=IntraoralScanImaging)
    photos: PhotosImaging = Field(default_factory=PhotosImaging)


class AiReadyContext(BaseModel):
    case_overview: str = ""
    known_information: list[str] = Field(default_factory=list)
    missing_information: list[str] = Field(default_factory=list)
    clinical_review_questions: list[str] = Field(default_factory=list)
    llm_prompt_context: str = ""


class Safety(BaseModel):
    not_for_diagnosis: bool = True
    requires_dentist_review: bool = True
    phi_removed: bool = True


class CasePacket(BaseModel):
    model_config = ConfigDict(extra="forbid")

    case_id: str
    created_at: datetime
    patient: Patient = Field(default_factory=Patient)
    chief_complaint: str = ""
    clinical_notes_summary: str = ""
    treatment_plan_summary: str = ""
    imaging: Imaging = Field(default_factory=Imaging)
    ai_ready_context: AiReadyContext = Field(default_factory=AiReadyContext)
    safety: Safety = Field(default_factory=Safety)


class FileManifestItem(BaseModel):
    file_type: str
    path: str
    sha256: str
    size_bytes: int
    extension: str
    role: str


class Manifest(BaseModel):
    created_at: datetime
    input_root: str
    files: list[FileManifestItem] = Field(default_factory=list)

