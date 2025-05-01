from datetime import datetime

from pywbmodels.common.enums import OrderMode
from pywbmodels.seller_analytics.card_stat.body.entity import CardStatBody
from pywbmodels.seller_analytics.card_stat.body.enums import CardStatOrderByField
from pywbmodels.seller_analytics.card_stat.body.value_objects import CardStatPeriod, CardStatOrderBy


def test_card_stat_body():
    model = CardStatBody(
        period=CardStatPeriod(
            begin=datetime(2025, 4, 28, 0, 0, 0),
            end=datetime(2025, 4, 28, 23, 59, 59),
        ),
        order_by=CardStatOrderBy(
            field=CardStatOrderByField.OPEN_CARD,
            mode=OrderMode.DESC,
        ),
        page=1,
    )

    assert model.model_dump() == {
        "period": {
            "begin": "2025-04-28 00:00:00",
            "end": "2025-04-28 23:59:59",
        },
        "orderBy": {
            "field": "openCard",
            "mode": "desc",
        },
        "page": 1,
    }
