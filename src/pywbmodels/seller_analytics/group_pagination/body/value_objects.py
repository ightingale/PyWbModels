from dataclasses import dataclass

from pywbmodels.common.enums import OrderMode
from pywbmodels.seller_analytics.group_pagination.body.enums import OrderByField


@dataclass
class OrderBy:
    field: OrderByField
    mode: OrderMode
