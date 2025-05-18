from dataclasses import dataclass

from pywbmodels.common.value_objects import PeriodStart
from pywbmodels.seller_analytics.group_pagination.body.enums import PositionCluster
from pywbmodels.seller_analytics.group_pagination.body.value_objects import OrderBy


@dataclass
class GroupPaginationBody:
    current_period: PeriodStart
    order_by: OrderBy
    position_cluster: PositionCluster
    limit: int
    offset: int
