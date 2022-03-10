from ...models import Model

class SalesOrderItem(Model):
    endpoint = 'sales_order_items'

    def __init__(self, partNo: str,  whse: str, id: int = None, orderQty: int = None, committedQty: int = None, sellMeasure: str = None, unitPrice: float = None):
        self.id = id
        self.partNo = partNo
        self.whse = whse
        self.orderQty = orderQty
        self.committedQty = committedQty
        self.sellMeasure = sellMeasure
        self.unitPrice = unitPrice