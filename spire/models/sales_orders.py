from tokenize import String
from pykson import JsonObject, ObjectListField, StringField, IntegerField

class SalesOrder(JsonObject):
    endpoint = 'sales_orders'
    id = IntegerField()
    orderNo = StringField()

class SalesOrderList(JsonObject):
    endpoint = 'sales_orders'
    records = ObjectListField(SalesOrder)