from pywbmodels.common.retort import main_retort
from pywbmodels.statistics.sales.response.entity import Sale


def test_sales_response():
    data = [
        {
            "date": "2022-03-04T18:08:31",
            "lastChangeDate": "2022-03-06T10:11:07",
            "warehouseName": "Подольск",
            "warehouseType": "Склад продавца",
            "countryName": "Россия",
            "oblastOkrugName": "Центральный федеральный округ",
            "regionName": "Московская",
            "supplierArticle": "12345",
            "nmId": 1234567,
            "barcode": "123453559000",
            "category": "Бытовая техника",
            "subject": "Мультистайлеры",
            "brand": "Тест",
            "techSize": "0",
            "incomeID": 56735459,
            "isSupply": False,
            "isRealization": True,
            "totalPrice": 1887,
            "discountPercent": 18,
            "spp": 20,
            "paymentSaleAmount": 93,
            "forPay": 1284.01,
            "finishedPrice": 1145,
            "priceWithDisc": 1547,
            "saleID": "S9993700024",
            "sticker": "926912515",
            "gNumber": "34343462218572569531",
            "srid": "11.rf9ef11fce1684117b0nhj96222982382.3.0"
        }
    ]

    retort = main_retort

    for item in data:
        assert retort.load(item, Sale)
