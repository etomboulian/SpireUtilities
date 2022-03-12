import datetime
from . import Model
from customer import Customer
from sales_order_item import SalesOrderItem

class SalesOrder(Model):
    api_endpoint = 'sales_orders'

    def __init__(self, customer: Customer = None, items: SalesOrderItem = None, status: str = None, type: str = None, hold: bool = None, orderDate: datetime = None, requiredDate: datetime = None, customerPO: str = None):
        self.customer = customer
        self.status = status
        self.type = type
        self.hold = hold
        self.orderDate = orderDate
        self.requiredDate = requiredDate
        self.customerPO = customerPO
        self.items = items
        