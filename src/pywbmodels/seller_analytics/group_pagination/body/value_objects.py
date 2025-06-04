from dataclasses import dataclass

from pywbmodels.common.enums import OrderMode, OrderByField


@dataclass
class OrderBy:
    field: OrderByField
    mode: OrderMode
