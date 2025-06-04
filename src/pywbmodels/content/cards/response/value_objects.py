from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Photo:
    big: str | None = None
    c246x328: str | None = None
    c516x688: str | None = None
    square: str | None = None
    tm: str | None = None


@dataclass
class Dimension:
    length: float | None = None
    width: float | None = None
    height: float | None = None
    is_valid: bool | None = None


@dataclass
class Characteristic:
    id: int | None = None
    name: str | None = None
    value: list[Any] | Any | None = None


@dataclass
class Size:
    chrt_id: int | None = None
    tech_size: str | None = None
    skus: list[str] | None = None


@dataclass
class Tag:
    id: int
    name: str
    color: str


@dataclass
class Card:
    nm_id: int
    imt_id: int
    nm_uuid: str
    subject_id: int
    subject_name: str
    vendor_code: str
    brand: str | None = None
    title: str | None = None
    photos: list[Photo] | None = None
    video: str | None = None
    dimensions: Dimension | None = None
    characteristics: list[Characteristic] | None = None
    sizes: list[Size] | None = None
    tags: list[Tag] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
