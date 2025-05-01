from enum import StrEnum


class CardStatOrderByField(StrEnum):
    OPEN_CARD = "openCard"
    ADD_TO_CARD = "addToCard"
    ORDERS = "orders"
    AVG_RUB_PRICE = "avgRubPrice"
    ORDERS_SUM_RUB = "ordersSumRub"
    STOCK_MP_QTY = "stockMpQty"
    STOCK_WB_QTY = "stockWbQty"
    CANCEL_SUM_RUB = "cancelSumRub"
    CANCEL_COUNT = "cancelCount"
    BUYOUT_COUNT = "buyoutCount"
    BUYOUT_SUM_RUB = "buyoutSumRub"
