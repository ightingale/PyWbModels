from dataclasses import dataclass

from pywbmodels.seller_analytics.card_stat.response.value_objects import CardStatData


@dataclass
class CardStatResponse:
    data: CardStatData
