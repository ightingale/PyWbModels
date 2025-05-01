from dataclasses import dataclass

from pywbmodels.seller_analytics.card_stat.body.value_objects import CardStatPeriod, CardStatOrderBy


@dataclass
class CardStatBody:
    period: CardStatPeriod
    order_by: CardStatOrderBy
    page: int
