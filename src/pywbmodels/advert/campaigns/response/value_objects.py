from dataclasses import dataclass


@dataclass
class RawAdvertListItem:
    advert_id: int
    change_time: str


@dataclass
class RawAdvert:
    type: int
    status: int
    count: int
    advert_list: list[RawAdvertListItem]
