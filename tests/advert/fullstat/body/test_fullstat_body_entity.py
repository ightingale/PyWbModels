from pywbmodels.advert.fullstats.body.entity import FullStatBodyByDates
from pywbmodels.common.retort import main_retort


def test_fullstat_body():
    retort = main_retort

    model = FullStatBodyByDates(
        id=8960367,
        dates=["2023-10-07", "2023-10-06"]
    )

    data = {
        "id": 8960367,
        "dates": [
            "2023-10-07",
            "2023-10-06"
        ]
    }

    assert retort.dump(model) == data
    assert retort.load(data, FullStatBodyByDates) == model
