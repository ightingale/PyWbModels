from dataclasses import dataclass
from datetime import datetime

from pywbmodels.common.enums import OrderMode
from pywbmodels.seller_analytics.card_stat.body.enums import CardStatOrderByField


@dataclass
class CardStatPeriod:
    begin: datetime
    end: datetime

    # @field_serializer("begin", "end")
    # @classmethod
    # def serialize_datetime(cls, value: datetime) -> str:
    #     return value.isoformat(sep=" ")


@dataclass
class CardStatOrderBy:
    field: CardStatOrderByField
    mode: OrderMode
