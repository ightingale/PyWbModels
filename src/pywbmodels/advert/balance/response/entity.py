from dataclasses import dataclass


@dataclass
class AdvertBalance:
    cash: int
    netting: int
    total: int
