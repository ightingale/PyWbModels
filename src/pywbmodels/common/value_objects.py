from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Period:
    begin: datetime
    end: datetime


@dataclass
class PeriodStart:
    start: date
    end: date
