import datetime
from dataclasses import dataclass


@dataclass
class KeywordStat:
    clicks: int
    ctr: float
    keyword: str
    sum: float
    views: int


@dataclass
class KeywordData:
    date: datetime.date
    stats: list[KeywordStat]
