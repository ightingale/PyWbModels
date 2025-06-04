from dataclasses import dataclass

from pywbmodels.content.cards.body.value_objects import Cursor
from pywbmodels.content.cards.response.value_objects import Card


@dataclass
class CardsResponse:
    cards: list[Card]
    cursor: Cursor
