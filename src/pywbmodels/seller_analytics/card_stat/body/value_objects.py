from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_serializer

from pywbmodels.common.enums import OrderMode
from pywbmodels.seller_analytics.card_stat.body.enums import CardStatOrderByField


class CardStatPeriod(BaseModel):
    begin: datetime
    end: datetime

    @field_serializer("begin", "end")
    @classmethod
    def serialize_datetime(cls, value: datetime) -> str:
        return value.isoformat(sep=" ")


class CardStatOrderBy(BaseModel):
    field: CardStatOrderByField
    mode: OrderMode

    model_config = ConfigDict(use_enum_values=True)
