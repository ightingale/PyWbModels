from adaptix import Retort, name_mapping, NameStyle, dumper, P

from pywbmodels.seller_analytics.card_stat.body.value_objects import CardStatPeriod
from pywbmodels.seller_analytics.card_stat.response.value_objects import CardData

main_retort = Retort(
    recipe=[
        name_mapping(name_style=NameStyle.CAMEL),
        name_mapping(
            CardData,
            map={"nm_id": "nmID"}
        ),
        dumper(
            P[CardStatPeriod].begin | P[CardStatPeriod].end,
            lambda x: x.isoformat(sep=" ")
        )
    ],
)
