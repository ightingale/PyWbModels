from dataclasses import dataclass


@dataclass
class BasicMetrics:
    current: int | None = None
    dynamics: int | None = None


@dataclass
class Metrics(BasicMetrics):
    percentile: int | None = None


@dataclass
class SearchTextItem:
    text: str
    nm_id: int
    frequency: BasicMetrics
    vendor_code: str
    week_frequency: int
    avg_position: BasicMetrics
    median_position: BasicMetrics
    open_card: Metrics
    add_to_cart: Metrics
    open_to_cart: Metrics
    orders: Metrics
    cart_to_order: Metrics
    visibility: BasicMetrics


@dataclass
class SearchTextsItemsData:
    items: list[SearchTextItem]
