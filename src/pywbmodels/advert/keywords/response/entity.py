from dataclasses import dataclass

from pywbmodels.advert.keywords.response.value_objects import KeywordData


@dataclass
class Keyword:
    keywords: list[KeywordData]
