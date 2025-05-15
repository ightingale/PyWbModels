import json

from pywbmodels.advert.fullstats.response.entity import FullStatResponse
from pywbmodels.common.retort import main_retort


def test_card_stat_response():
    # model = FullStatResponse()

    retort = main_retort

    data = {
        "views": 1052,
        "clicks": 2,
        "ctr": 0.19,
        "cpc": 0.09,
        "sum": 177.7,
        "atbs": 0,
        "orders": 0,
        "cr": 0,
        "shks": 0,
        "sum_price": 0,
        "dates": [
            "2023-10-07",
            "2023-10-06"
        ],
        "days": [
            {
                "date": "2023-10-06T03:00:00+03:00",
                "views": 414,
                "clicks": 1,
                "ctr": 0.24,
                "cpc": 70,
                "sum": 70,
                "atbs": 0,
                "orders": 0,
                "cr": 0,
                "shks": 0,
                "sum_price": 0,
                "apps": [
                    {
                        "views": 228,
                        "clicks": 0,
                        "ctr": 0,
                        "cpc": 0,
                        "sum": 38.71,
                        "atbs": 0,
                        "orders": 0,
                        "cr": 0,
                        "shks": 0,
                        "sum_price": 0,
                        "nm": [
                            {
                                "views": 25,
                                "clicks": 0,
                                "ctr": 0,
                                "cpc": 0,
                                "sum": 4,
                                "atbs": 0,
                                "orders": 0,
                                "cr": 0,
                                "shks": 0,
                                "sum_price": 0,
                                "name": "Тапочки",
                                "nmId": 111111111111
                            }
                        ],
                        "appType": 1
                    }
                ]
            }
        ],
        "boosterStats": [
            {
                "date": "2023-10-07T00:00:00Z",
                "nm": 170095908,
                "avg_position": 348
            }
        ],
        "advertId": 10524818
    }
    assert retort.load(data, FullStatResponse)


def test_card_stat_response_with_real_data():
    retort = main_retort

    with open("full_stat_response.json", encoding="utf-8") as file:
        data = json.load(file)

    assert retort.load(data, FullStatResponse)
