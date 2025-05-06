from dataclasses import dataclass


@dataclass
class ProductAnalytics:
    name: str
    nm_id: int


@dataclass
class AppData:
    nm: list[ProductAnalytics]
    app_type: int | None


@dataclass
class FullStatDay:
    date: str
    views: int
    clicks: int
    ctr: float
    cpc: float
    sum: float
    atbs: int
    orders: int
    cr: float
    shks: int
    sum_price: float
    apps: list[AppData]


@dataclass
class BoosterStats:
    date: str
    nm: int
    avg_position: int
