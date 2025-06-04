from dataclasses import dataclass

from pywbmodels.content.cards.response.value_objects import Card, ResponseCursor


@dataclass
class CardsResponse:
    cards: list[Card]
    cursor: ResponseCursor
