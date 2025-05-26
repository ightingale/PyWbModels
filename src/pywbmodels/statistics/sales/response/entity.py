from dataclasses import dataclass
from datetime import datetime

from pywbmodels.statistics.sales.response.enums.warehouse import WarehouseType


@dataclass
class Sale:
    date: datetime
    last_change_date: datetime
    warehouse_name: str
    warehouse_type: WarehouseType
    country_name: str
    oblast_okrug_name: str
    region_name: str
    supplier_article: str
    nm_id: int
    barcode: str
    category: str
    subject: str
    brand: str
    tech_size: str
    income_id: int
    is_supply: bool
    is_realization: bool
    total_price: float
    discount_percent: float
    spp: float
    for_pay: float
    finished_price: float
    price_with_disc: float
    sale_id: str
    sticker: str
    g_number: str
    srid: str
