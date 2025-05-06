from dataclasses import dataclass


@dataclass
class FullStatBodyByDates:
    id: int
    dates: list[str]
