from enum import Enum


class AdvertStatus(Enum):
    READY_TO_LAUNCH = 4
    CAMPAIGN_COMPLETED = 7
    DECLINED = 8
    SHOWING_IN_PROGRESS = 9
    PAUSED = 11


class AdvertType(Enum):
    AUTOMATIC_CAMPAIGN = 8
    AUCTION = 9
