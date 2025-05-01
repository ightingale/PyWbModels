from dataclasses import dataclass

from pywbmodels.seller_analytics.card_stat.response.value_objects import CardData


@dataclass
class CardStatResponse:
    cards: list[CardData]
