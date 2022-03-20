from marshmallow_dataclass import dataclass
from typing import Optional, List

from .inventory import UOM

@dataclass
class SalesOrderItem:
    id: int
    whse: str
    partNo: str
    orderQty: float
    committedQty: float
    sellMeasure: UOM
    unitPrice: float