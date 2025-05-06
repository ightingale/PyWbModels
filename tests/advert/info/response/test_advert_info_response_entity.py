from pywbmodels.advert.info.response.entity import AdvertInfoResponse
from pywbmodels.advert.info.response.enums import AdvertType, AdvertStatus
from pywbmodels.advert.info.response.value_objects import AutoParams, NmCpm, Active, Subject
from pywbmodels.common.retort import main_retort


def test_advert_info_response():
    retort = main_retort

    model = AdvertInfoResponse(
        end_time="2023-10-05T21:37:37.226021+03:00",
        create_time="2023-08-21T13:45:31.121172+03:00",
        change_time="2023-08-21T14:59:33.622594+03:00",
        start_time="2023-08-21T13:45:31.147601+03:00",
        auto_params=AutoParams(
            nm_cpm=[
                NmCpm(
                    nm=1234567,
                    cpm=150
                )
            ],
            active=Active(
                carousel=True,
                recom=True,
                booster=True
            ),
            nms=[1234567],
            sets=[
                Subject(
                    name="для женщин",
                    id=623
                )
            ],
            subject=Subject(
                name="Обложки",
                id=342
            )
        ),
        name="Кампания1",
        daily_budget=0,
        advert_id=11111111,
        status=AdvertStatus.CAMPAIGN_COMPLETED,
        type=AdvertType.AUTOMATIC_CAMPAIGN,
        payment_type="cpm",
    )

    data = {
        "endTime": "2023-10-05T21:37:37.226021+03:00",
        "createTime": "2023-08-21T13:45:31.121172+03:00",
        "changeTime": "2023-08-21T14:59:33.622594+03:00",
        "startTime": "2023-08-21T13:45:31.147601+03:00",
        "autoParams": {
            "subject": {
                "name": "Обложки",
                "id": 342
            },
            "sets": [
                {
                    "name": "для женщин",
                    "id": 623
                }
            ],
            "nms": [
                1234567
            ],
            "active": {
                "carousel": True,
                "recom": True,
                "booster": True
            },
            "nmCPM": [
                {
                    "nm": 1234567,
                    "cpm": 150
                }
            ]
        },
        "name": "Кампания1",
        "dailyBudget": 0,
        "advertId": 11111111,
        "status": 7,
        "type": 8,
        "paymentType": "cpm"
    }

    assert retort.load(data, AdvertInfoResponse) == model

