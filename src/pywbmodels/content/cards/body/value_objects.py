from dataclasses import dataclass


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


@dataclass
class CardsBodySettings:
    sort: Sort
    filter: Filter
    cursor: Cursor
