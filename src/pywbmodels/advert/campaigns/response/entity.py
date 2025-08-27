from dataclasses import dataclass

from pywbmodels.advert.campaigns.response.value_objects import RawAdvert


@dataclass
class AdvertCampaignsResponse:
    adverts: list[RawAdvert] | None
    all: int
