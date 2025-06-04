from enum import StrEnum


class OrderMode(StrEnum):
    ASC = "asc"
    DESC = "desc"


class OrderByField(StrEnum):
    AVG_POSITION = "avgPosition"
    ADD_TO_CARD = "addToCard"
    OPEN_CARD = "openCard"
    ORDERS = "orders"
    CART_TO_ORDER = "cartToOrder"
    OPEN_TO_CART = "openToCart"
    VISIBILITY = "visibility"
