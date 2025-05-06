from dataclasses import dataclass

from pywbmodels.advert.fullstats.response.value_objects import FullStatDay, BoosterStats


@dataclass
class FullStatResponse:
    views: int
    clicks: int
    ctr: float
    cpc: float
    sum: float
    atbs: int
    orders: int
    cr: float
    shks: int
    sum_price: float
    dates: list[str]
    days: list[FullStatDay]
    booster_stats: list[BoosterStats]
    advert_id: int
