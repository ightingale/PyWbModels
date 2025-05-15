from adaptix import Retort, name_mapping, NameStyle, dumper, P

from pywbmodels.advert.campaigns.response.value_objects import RawAdvert
from pywbmodels.advert.fullstats.response.entity import FullStatResponse
from pywbmodels.advert.fullstats.response.value_objects import BoosterStats, FullStatDay
from pywbmodels.advert.info.response.value_objects import AutoParams
from pywbmodels.common.value_objects import Period
from pywbmodels.seller_analytics.card_stat.response.value_objects import CardData

main_retort = Retort(
    recipe=[
        name_mapping(
            BoosterStats,
            map={"avg_position": "avg_position"},
        ),
        name_mapping(
            FullStatDay,
            map={"sum_price": "sum_price"},
        ),
        name_mapping(
            FullStatResponse,
            map={"sum_price": "sum_price"},
        ),
        name_mapping(
            RawAdvert,
            map={"advert_list": "advert_list"},
        ),
        name_mapping(name_style=NameStyle.CAMEL, omit_default=True),
        name_mapping(
            CardData,
            map={"nm_id": "nmID"}
        ),
        name_mapping(
            AutoParams,
            map={"nm_cpm": "nmCPM"}
        ),
        dumper(
            P[Period].begin |
            P[Period].end,
            lambda x: x.isoformat(sep=" ")
        )
    ],
)
