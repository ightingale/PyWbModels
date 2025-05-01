from dataclasses import dataclass, Field


@dataclass
class Conversions:
    add_to_cart_percent: int
    cart_to_order_percent: int
    buyouts_percent: int


@dataclass
class PeriodData:
    begin: str
    end: str
    open_card_count: int = Field(..., alias="openCardCount")
    add_to_cart_count: int = Field(..., alias="addToCartCount")
    orders_count: int = Field(..., alias="ordersCount")
    orders_sum_rub: int = Field(..., alias="ordersSumRub")
    buyouts_count: int = Field(..., alias="buyoutsCount")
    buyouts_sum_rub: int = Field(..., alias="buyoutsSumRub")
    cancel_count: int = Field(..., alias="cancelCount")
    cancel_sum_rub: int = Field(..., alias="cancelSumRub")
    avg_orders_count_per_day: int | float = Field(..., alias="avgOrdersCountPerDay")
    avg_price_rub: int = Field(..., alias="avgPriceRub")
    conversions: Conversions


@dataclass
class PeriodComparison:
    open_card_dynamics: int = Field(..., alias="openCardDynamics")
    add_to_cart_dynamics: int = Field(..., alias="addToCartDynamics")
    orders_count_dynamics: int = Field(..., alias="ordersCountDynamics")
    orders_sum_rub_dynamics: int = Field(..., alias="ordersSumRubDynamics")
    buyouts_count_dynamics: int = Field(..., alias="buyoutsCountDynamics")
    buyouts_sum_rub_dynamics: int = Field(..., alias="buyoutsSumRubDynamics")
    cancel_count_dynamics: int = Field(..., alias="cancelCountDynamics")
    cancel_sum_rub_dynamics: int = Field(..., alias="cancelSumRubDynamics")
    avg_orders_count_per_day_dynamics: int = Field(..., alias="avgOrdersCountPerDayDynamics")
    avg_price_rub_dynamics: int = Field(..., alias="avgPriceRubDynamics")
    conversions: Conversions


@dataclass
class Statistics:
    selected_period: PeriodData = Field(..., alias="selectedPeriod")
    previous_period: PeriodData = Field(..., alias="previousPeriod")
    period_comparison: PeriodComparison = Field(..., alias="periodComparison")


@dataclass
class Stocks:
    stocks_wb: int | None = Field(..., alias="stocksWb")


@dataclass
class ObjectData:
    name: str


@dataclass
class CardData:
    nm_id: int = Field(..., alias="nmID")
    vendor_code: str = Field(..., alias="vendorCode")
    brand_name: str = Field(..., alias="brandName")
    object: ObjectData
    statistics: Statistics
    stocks: Stocks
