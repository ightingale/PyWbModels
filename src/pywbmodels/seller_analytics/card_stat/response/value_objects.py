from dataclasses import dataclass


@dataclass
class Conversions:
    add_to_cart_percent: int
    cart_to_order_percent: int
    buyouts_percent: int


@dataclass
class PeriodData:
    begin: str
    end: str
    open_card_count: int
    add_to_cart_count: int
    orders_count: int
    orders_sum_rub: int
    buyouts_count: int
    buyouts_sum_rub: int
    cancel_count: int
    cancel_sum_rub: int
    avg_orders_count_per_day: int | float
    avg_price_rub: int
    conversions: Conversions


@dataclass
class PeriodComparison:
    open_card_dynamics: int
    add_to_cart_dynamics: int
    orders_count_dynamics: int
    orders_sum_rub_dynamics: int
    buyouts_count_dynamics: int
    buyouts_sum_rub_dynamics: int
    cancel_count_dynamics: int
    cancel_sum_rub_dynamics: int
    avg_orders_count_per_day_dynamics: int
    avg_price_rub_dynamics: int
    conversions: Conversions


@dataclass
class Statistics:
    selected_period: PeriodData
    previous_period: PeriodData
    period_comparison: PeriodComparison


@dataclass
class Stocks:
    stocks_wb: int | None


@dataclass
class ObjectData:
    name: str


@dataclass
class CardData:
    nm_id: int
    vendor_code: str
    brand_name: str
    object: ObjectData
    statistics: Statistics
    stocks: Stocks


@dataclass
class CardStatData:
    cards: list[CardData]
