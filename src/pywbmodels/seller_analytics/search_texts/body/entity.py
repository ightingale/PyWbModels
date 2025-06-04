from dataclasses import dataclass

from pywbmodels.common.value_objects import PeriodStart, OrderBy
from pywbmodels.common.enums import OrderByField


@dataclass
class SearchTextsBody:
    current_period: PeriodStart
    nm_ids: list[int]
    top_order_by: OrderByField
    order_by: OrderBy
    limit: int
