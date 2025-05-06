from dataclasses import dataclass, Field

from pywbmodels.advert.info.response.enums import AdvertType, AdvertStatus
from pywbmodels.advert.info.response.value_objects import Params, UnitedParams, AutoParams


@dataclass
class AdvertInfoResponse:
    end_time: str
    create_time: str
    change_time: str
    start_time: str
    name: str
    daily_budget: int
    advert_id: int
    status: AdvertStatus
    type: AdvertType
    payment_type: str
    auto_params: AutoParams | None = None
    united_params: list[UnitedParams] | None = None
    params: list[Params] | None = None
