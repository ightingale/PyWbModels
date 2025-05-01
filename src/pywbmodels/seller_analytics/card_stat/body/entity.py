from pydantic import BaseModel, Field, ConfigDict

from pywbmodels.seller_analytics.card_stat.body.value_objects import CardStatPeriod, CardStatOrderBy


class CardStatBody(BaseModel):
    period: CardStatPeriod
    order_by: CardStatOrderBy = Field(..., serialization_alias="orderBy")
    page: int

    model_config = ConfigDict(serialize_by_alias=True)
