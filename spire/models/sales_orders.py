from tokenize import String
from pykson import JsonObject, ObjectListField, ObjectField, StringField, IntegerField, DateField, FloatField, BooleanField

from spire.models.customers import Customer

class SalesOrder(JsonObject):
    endpoint = 'sales_orders'
    id = IntegerField()
    orderNo = StringField()
    customer = ObjectField(Customer)
    status = StringField()
    type = StringField()
    invoiceDate = DateField()
    requiredDate = DateField()
    customerPO = StringField()
    batchNo = StringField()
    division = StringField()
    location = StringField()
    profitCenter = StringField()
    incoterms = StringField()
    incotermsPlace = StringField()
    salespersonNo = StringField()
    territoryCode = StringField()
    freight = FloatField()
    weight = FloatField()
    dicount = FloatField()
    totalDiscount = FloatField()
    subtotal = FloatField()
    total = FloatField()
    baseTotal = FloatField()
    total2 = FloatField()
    totalOrdered = FloatField()
    backordered = BooleanField()
    totalBackorderQty = FloatField()
    grossProfit = FloatField()
    grossProfitMargin = FloatField()
    grossProfit2 = FloatField()
    totalCostAverage = FloatField()
    totalCostAverage2 = FloatField()
    totalCostCurrent = FloatField()
    totalCostCurrent2 = FloatField()
    totalCostStandard = FloatField()
    totalCostStandard2 = FloatField()
    phaseId = StringField()
    termsCode = StringField()
    termsText = StringField()
    referenceNo = StringField()
    currency = StringField()
    shippingCarrier = StringField()
    shipDate = StringField()
    trackingNo = StringField()
    jobNo = StringField()

class SalesOrderList(JsonObject):
    metadata = {
        'endpoint': 'sales_orders'
    }
    records = ObjectListField(SalesOrder)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()