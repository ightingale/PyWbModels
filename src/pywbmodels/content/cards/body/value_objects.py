
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sort:
    ascending: bool


@dataclass
class Filter:
    text_search: str
    allow_categories_only: bool
    tag_ids: list[int]
    object_ids: list[int]
    brands: list[int]
    imt_id: int
    with_photo: int


@dataclass
class Cursor:
    limit: int
    updated_at: datetime | None = None
    nm_id: int | None = None
    total: int | None = None


@dataclass
class CardsBodySettings:
    sort: Sort
    filter: Filter
    cursor: Cursor
