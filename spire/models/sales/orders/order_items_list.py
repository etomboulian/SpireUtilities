from pykson import JsonField, JsonObject, ObjectField, ObjectListField, IntegerField, StringField, BooleanField, FloatField, DateField, DateTimeField
from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/sales/items/
# Allows: [GET, HEAD, OPTIONS]

class Customer(JsonObject):
    customerNo = StringField()
    name = StringField()
    foregroundColor = IntegerField()
    backgroundColor = IntegerField()

class ShippingAddress(JsonObject):
    shipId = StringField()
    name = StringField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    postalCode = StringField()
    shipCode = StringField()
    shipDescription = StringField()

class Order(JsonObject):
    id = IntegerField()
    hold = BooleanField()
    status = StringField()
    type = StringField()
    orderDate = DateField()
    customer = ObjectField(Customer)
    customerPO = StringField()
    invoiceNo = StringField()
    invoiceDate = DateField()
    batchNo = StringField()
    subtotal = FloatField(accepts_string=True)
    total = FloatField(accepts_string=True)
    baseTotal = FloatField(accepts_string=True)
    total2 = FloatField(accepts_string=True)
    subTotal2 = FloatField(accepts_string=True)
    backordered = BooleanField()
    grossProfit = FloatField(accepts_string=True)
    grossProfitMargin = FloatField(accepts_string=True)
    grossProfit2 = FloatField(accepts_string=True)
    totalCostCurrent = FloatField(accepts_string=True)
    totalCostAverage = FloatField(accepts_string=True)
    totalCostAverage2 = FloatField(accepts_string=True)
    totalCostCurrent2 = FloatField(accepts_string=True)
    shippingAddress = ObjectField(ShippingAddress)
    fob = StringField()
    salespersonNo = StringField()
    division = StringField()
    location = StringField()
    territoryCode = StringField()
    shipCode = StringField()
    requiredDate = DateField()
    shipDate = DateField()
    termsCode = StringField()
    termsText = StringField()
    referenceNo = StringField()
    currency = StringField()
    modifiedBy = StringField()
    createdBy = StringField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')


class SalesOrderItem(JsonObject, EditableObject):
    metadata = {
        'endpoint': 'sales_orders/items'
    }
    id = IntegerField()
    orderNo = StringField()
    sequence = IntegerField()
    whse = StringField()
    partNo = StringField()
    itemType = IntegerField()
    description = StringField()
    comment = StringField()
    orderQty = IntegerField(accepts_string=True)
    committedQty = IntegerField(accepts_string=True)
    backorderQty = IntegerField(accepts_string=True)
    retailPrice = FloatField(accepts_string=True)
    lineDiscountPct = FloatField(accepts_string=True)
    discountPct = FloatField(accepts_string=True)
    unitPrice = FloatField(accepts_string=True)
    extendedPriceOrdered = FloatField(accepts_string=True)
    sellMeasure = StringField()
    vendor = StringField()
    levyCode = StringField()
    inventoryGroupNo = StringField()
    requiredDate = DateField()
    suppress = BooleanField()
    averageCost = FloatField(accepts_string=True)
    currentCost = FloatField(accepts_string=True)
    standardCost = FloatField(accepts_string=True)
    weight = FloatField(accepts_string=True)
    employeeNo = StringField()
    jobNo = StringField()
    jobAccountNo = StringField()
    modifiedBy = StringField()
    createdBy = StringField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    order = ObjectField(Order)


class SalesOrderItemList(JsonObject):
    metadata = {
        'endpoint': 'sales_orders/items'
    }
    records = ObjectListField(SalesOrderItem)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()