from dataclasses import dataclass
from datetime import datetime, date

from pywbmodels.common.enums import OrderMode, OrderByField


@dataclass
class Period:
    begin: datetime
    end: datetime


@dataclass
class PeriodStart:
    start: date
    end: date


@dataclass
class OrderBy:
    field: OrderByField
    mode: OrderMode
