from pywbmodels.advert.campaigns.response.entity import AdvertCampaignsResponse
from pywbmodels.advert.campaigns.response.value_objects import RawAdvert, RawAdvertListItem
from pywbmodels.advert.info.response.enums import AdvertType, AdvertStatus
from pywbmodels.common.retort import main_retort


def test_card_stat_response():
    retort = main_retort

    model = AdvertCampaignsResponse(
        adverts=[
            RawAdvert(
                type=AdvertType.AUTOMATIC_CAMPAIGN,
                status=AdvertStatus.DECLINED,
                count=3,
                advert_list=[
                    RawAdvertListItem(
                        advert_id=6485174,
                        change_time="2023-05-10T12:12:52.676254+03:00"
                    ),
                    RawAdvertListItem(
                        advert_id=6500443,
                        change_time="2023-05-10T17:08:46.370656+03:00"
                    ),
                    RawAdvertListItem(
                        advert_id=7936341,
                        change_time="2023-07-12T15:51:08.367478+03:00"
                    )
                ]
            )
        ],
        all=3
    )

    data = {
        "adverts": [
            {
                "type": 8,
                "status": 8,
                "count": 3,
                "advert_list": [
                    {
                        "advertId": 6485174,
                        "changeTime": "2023-05-10T12:12:52.676254+03:00"
                    },
                    {
                        "advertId": 6500443,
                        "changeTime": "2023-05-10T17:08:46.370656+03:00"
                    },
                    {
                        "advertId": 7936341,
                        "changeTime": "2023-07-12T15:51:08.367478+03:00"
                    }
                ]
            }
        ],
        "all": 3
    }

    assert retort.load(data, AdvertCampaignsResponse) == model
