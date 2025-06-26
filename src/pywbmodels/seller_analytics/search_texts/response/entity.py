import datetime
from dataclasses import dataclass

from adaptix import Omitted

from pywbmodels.seller_analytics.search_texts.response.value_objects import SearchTextsItemsData


@dataclass
class SearchTextsResponse:
    data: SearchTextsItemsData
    period: datetime.date = Omitted()
