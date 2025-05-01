from dataclasses import dataclass
from datetime import datetime

from pywbmodels.common.enums import OrderMode
from pywbmodels.seller_analytics.card_stat.body.enums import CardStatOrderByField


@dataclass
class CardStatPeriod:
    begin: datetime
    end: datetime


@dataclass
class CardStatOrderBy:
    field: CardStatOrderByField
    mode: OrderMode
