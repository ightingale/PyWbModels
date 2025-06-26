from adaptix import Retort, name_mapping, NameStyle, dumper, P

from pywbmodels.advert.campaigns.response.value_objects import RawAdvert
from pywbmodels.advert.fullstats.response.entity import FullStatResponse
from pywbmodels.advert.fullstats.response.value_objects import BoosterStats, FullStatDay
from pywbmodels.advert.info.response.value_objects import AutoParams, UnitedParams
from pywbmodels.common.value_objects import Period
from pywbmodels.content.cards.body.value_objects import Cursor
from pywbmodels.content.cards.response.entity import Card
from pywbmodels.content.cards.response.value_objects import Size
from pywbmodels.seller_analytics.card_stat.response.value_objects import CardData
from pywbmodels.statistics.orders.response.entity import Order
from pywbmodels.statistics.sales.response.entity import Sale

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
        name_mapping(
            Size,
            map={"chrt_id": "chrtID"}
        ),
        name_mapping(
            Card,
            map={
                "nm_id": "nmID",
                "imt_id": "imtID",
                "nm_uuid": "nmUUID",
                "subject_id": "subjectID",
            }
        ),
        name_mapping(
            Cursor,
            map={"nm_id": "nmID"}
        ),
        name_mapping(
            Sale,
            map={"sale_id": "saleID", "income_id": "incomeID"}
        ),
        name_mapping(
            Order,
            map={"income_id": "incomeID"}
        ),
        name_mapping(
            UnitedParams,
            map={
                "search_cpm": "searchCPM",
                "catalog_cpm": "catalogCPM",
            }
        ),
        dumper(
            P[Period].begin |
            P[Period].end,
            lambda x: x.isoformat(sep=" ")
        )
    ],
)
