from dataclasses import dataclass

from pywbmodels.content.cards.body.value_objects import CardsBodySettings


@dataclass
class CardsBody:
    settings: CardsBodySettings
