from dataclasses import dataclass

from pywbmodels.common.enums import OrderMode
from pywbmodels.seller_analytics.card_stat.body.enums import CardStatOrderByField


@dataclass
class CardStatOrderBy:
    field: CardStatOrderByField
    mode: OrderMode
