from datetime import datetime
from marshmallow_dataclass import dataclass
from typing import Optional, List

from .customer import Customer
from .sales_order_item import SalesOrderItem

@dataclass
class SalesOrder:
    customer: Customer
    status: str
    type: str
    hold: bool
    orderDate: datetime
    requiredDate: datetime
    customerPO: str
    items: List[SalesOrderItem] 
        
@dataclass
class SalesOrderList:
    records: Optional[List[SalesOrder]]
    start: Optional[int]
    limit: Optional[int]
    count: Optional[int]