from dataclasses import dataclass

from pywbmodels.seller_analytics.card_stat.body.value_objects import CardStatOrderBy
from pywbmodels.common.value_objects import Period


@dataclass
class CardStatBody:
    period: Period
    order_by: CardStatOrderBy
    page: int
