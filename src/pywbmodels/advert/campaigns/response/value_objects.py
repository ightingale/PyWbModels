from dataclasses import dataclass

from pywbmodels.advert.info.response.enums import AdvertType, AdvertStatus


@dataclass
class RawAdvertListItem:
    advert_id: int
    change_time: str


@dataclass
class RawAdvert:
    type: AdvertType
    status: AdvertStatus
    count: int
    advert_list: list[RawAdvertListItem]
