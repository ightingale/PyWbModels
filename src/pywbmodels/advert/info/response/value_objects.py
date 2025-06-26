from dataclasses import dataclass

from adaptix import Omitted


@dataclass
class Nm:
    nm: int
    active: bool


@dataclass
class Params:
    nms: list[Nm]


@dataclass
class Subject:
    id: int
    name: str


@dataclass
class UnitedParams:
    catalog_cpm: int
    search_cpm: int
    subject: Subject
    menus: list[Subject]
    nms: list[int]


@dataclass
class Active:
    carousel: bool
    recom: bool
    booster: bool


@dataclass
class NmCpm:
    nm: int
    cpm: int


@dataclass
class AutoParams:
    cpm: int
    nm_cpm: list[NmCpm]
    subject: Subject
    nms: list[int]
    active: Active
    sets: list[Subject] = Omitted()
