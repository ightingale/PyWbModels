from adaptix import Retort, name_mapping, NameStyle

from pywbmodels.seller_analytics.card_stat.response.entity import CardStatResponse
from pywbmodels.seller_analytics.card_stat.response.value_objects import CardData, ObjectData, Statistics, PeriodData, \
    Conversions, PeriodComparison, Stocks


# noinspection PyArgumentList
def test_card_stat_response():
    model = CardStatResponse(
        cards=[
            CardData(
                nm_id=12345678,
                vendor_code="VC-00123",
                brand_name="TestBrand",
                object=ObjectData(
                    name="Футболка"
                ),
                statistics=Statistics(
                    selected_period=PeriodData(
                        begin="2025-04-01",
                        end="2025-04-30",
                        open_card_count=1500,
                        add_to_cart_count=800,
                        orders_count=300,
                        orders_sum_rub=450000,
                        buyouts_count=250,
                        buyouts_sum_rub=375000,
                        cancel_count=20,
                        cancel_sum_rub=30000,
                        avg_orders_count_per_day=10,
                        avg_price_rub=1500,
                        conversions=Conversions(
                            add_to_cart_percent=53,
                            cart_to_order_percent=37,
                            buyouts_percent=83
                        )
                    ),
                    previous_period=PeriodData(
                        begin="2025-03-01",
                        end="2025-03-31",
                        open_card_count=1200,
                        add_to_cart_count=600,
                        orders_count=200,
                        orders_sum_rub=300000,
                        buyouts_count=160,
                        buyouts_sum_rub=240000,
                        cancel_count=25,
                        cancel_sum_rub=37500,
                        avg_orders_count_per_day=6.5,
                        avg_price_rub=1500,
                        conversions=Conversions(
                            add_to_cart_percent=50,
                            cart_to_order_percent=33,
                            buyouts_percent=80
                        )
                    ),
                    period_comparison=PeriodComparison(
                        open_card_dynamics=25,
                        add_to_cart_dynamics=33,
                        orders_count_dynamics=50,
                        orders_sum_rub_dynamics=50,
                        buyouts_count_dynamics=56,
                        buyouts_sum_rub_dynamics=56,
                        cancel_count_dynamics=-20,
                        cancel_sum_rub_dynamics=-20,
                        avg_orders_count_per_day_dynamics=54,
                        avg_price_rub_dynamics=0,
                        conversions=Conversions(
                            add_to_cart_percent=3,
                            cart_to_order_percent=4,
                            buyouts_percent=3
                        )
                    )
                ),
                stocks=Stocks(
                    stocks_wb=350
                )
            )
        ]
    )

    retort = Retort(
        recipe=[
            name_mapping(
                name_style=NameStyle.CAMEL,
            ),
            name_mapping(
                CardData,
                map={
                    "nm_id": "nmID",
                }
            )
        ],
    )

    data = {
        "cards": [
            {
                "nmID": 12345678,
                "vendorCode": "VC-00123",
                "brandName": "TestBrand",
                "object": {
                    "name": "Футболка"
                },
                "statistics": {
                    "selectedPeriod": {
                        "begin": "2025-04-01",
                        "end": "2025-04-30",
                        "openCardCount": 1500,
                        "addToCartCount": 800,
                        "ordersCount": 300,
                        "ordersSumRub": 450000,
                        "buyoutsCount": 250,
                        "buyoutsSumRub": 375000,
                        "cancelCount": 20,
                        "cancelSumRub": 30000,
                        "avgOrdersCountPerDay": 10,
                        "avgPriceRub": 1500,
                        "conversions": {
                            "addToCartPercent": 53,
                            "cartToOrderPercent": 37,
                            "buyoutsPercent": 83
                        }
                    },
                    "previousPeriod": {
                        "begin": "2025-03-01",
                        "end": "2025-03-31",
                        "openCardCount": 1200,
                        "addToCartCount": 600,
                        "ordersCount": 200,
                        "ordersSumRub": 300000,
                        "buyoutsCount": 160,
                        "buyoutsSumRub": 240000,
                        "cancelCount": 25,
                        "cancelSumRub": 37500,
                        "avgOrdersCountPerDay": 6.5,
                        "avgPriceRub": 1500,
                        "conversions": {
                            "addToCartPercent": 50,
                            "cartToOrderPercent": 33,
                            "buyoutsPercent": 80
                        }
                    },
                    "periodComparison": {
                        "openCardDynamics": 25,
                        "addToCartDynamics": 33,
                        "ordersCountDynamics": 50,
                        "ordersSumRubDynamics": 50,
                        "buyoutsCountDynamics": 56,
                        "buyoutsSumRubDynamics": 56,
                        "cancelCountDynamics": -20,
                        "cancelSumRubDynamics": -20,
                        "avgOrdersCountPerDayDynamics": 54,
                        "avgPriceRubDynamics": 0,
                        "conversions": {
                            "addToCartPercent": 3,
                            "cartToOrderPercent": 4,
                            "buyoutsPercent": 3
                        }
                    }
                },
                "stocks": {
                    "stocksWb": 350
                },
            }
        ]
    }

    assert retort.dump(model) == data
    assert retort.load(data, CardStatResponse) == model
