from pykson import JsonObject, JsonField, ObjectListField, ObjectField, StringField, IntegerField, DateField, FloatField, BooleanField, DateTimeField
from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/sales/orders/
# Allows: [GET, HEAD, OPTIONS, POST]

class OrderAddress(JsonObject):
    id = IntegerField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    provState = StringField()
    postalCode = StringField()
    country = StringField()

class OrderShippingAddress(JsonObject):
    id = IntegerField()
    shipId = StringField()
    name = StringField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    provState = StringField()
    postalCode = StringField()
    country = StringField()
    shipCode = StringField()
    shipDescription = StringField()

class PhoneNumber(JsonObject):
    number = StringField()
    format = IntegerField()

class OrderContact(JsonObject):
    name = StringField()
    email = StringField()
    phone = ObjectField(PhoneNumber)
    fax = ObjectField(PhoneNumber)

class Customer(JsonObject):
    id = IntegerField()
    customerNo = StringField()
    name = StringField()
    userDef2 = StringField()
    invoiceType = StringField()
    hold = BooleanField()
    foregroundColor = IntegerField()
    backgroundColor = IntegerField()

class SalesOrder(JsonObject, EditableObject):
    metadata = { 
        'endpoint': 'sales_orders', 
        'allowed_methods': ['GET', 'POST']
        }
    id = IntegerField()
    orderNo = StringField()
    invoiceNo = StringField()
    customer = ObjectField(Customer)
    status = StringField()
    type = StringField()
    hold = BooleanField()
    orderDate = DateField()
    invoiceDate = DateField()
    requiredDate = DateField()
    customerPO = StringField()
    batchNo = StringField()
    division = StringField()
    location = StringField()
    profitCenter = StringField()
    fob = StringField()
    incoterms = StringField()
    incotermsPlace = StringField()
    salespersonNo = StringField()
    territoryCode = StringField()
    freight = FloatField(accepts_string=True)
    weight = FloatField(accepts_string=True)
    discount = FloatField(accepts_string=True)
    totalDiscount = FloatField(accepts_string=True)
    subtotal = FloatField(accepts_string=True)
    subtotalOrdered = FloatField(accepts_string=True)
    total = FloatField(accepts_string=True)
    baseTotal = FloatField(accepts_string=True)
    total2 = FloatField(accepts_string=True)
    totalOrdered = FloatField(accepts_string=True)
    backordered = BooleanField(accepts_string=True)
    totalBackorderQty = FloatField(accepts_string=True)
    grossProfit = FloatField(accepts_string=True)
    grossProfitMargin = FloatField(accepts_string=True)
    grossProfit2 = FloatField(accepts_string=True)
    totalCostAverage = FloatField(accepts_string=True)
    totalCostAverage2 = FloatField(accepts_string=True)
    totalCostCurrent = FloatField(accepts_string=True)
    totalCostCurrent2 = FloatField(accepts_string=True)
    totalCostStandard = FloatField(accepts_string=True)
    totalCostStandard2 = FloatField(accepts_string=True)
    phaseId = StringField()
    termsCode = StringField()
    termsText = StringField()
    referenceNo = StringField()
    currency = StringField()
    shippingCarrier = StringField()
    shipDate = StringField()
    trackingNo = StringField()
    jobNo = StringField()
    jobAccountNo = StringField()
    wasQuoteNo = StringField()
    amountPaid = FloatField()
    amountUnpaid = FloatField()
    amountUnpaidOrdered = FloatField()
    percentPaid = StringField()
    address = ObjectField(OrderAddress)
    shippingAddress = ObjectField(OrderShippingAddress)
    contact = ObjectField(OrderContact)
    deleted = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    deletedBy = StringField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    createdBy = StringField()
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modifiedBy = StringField()
    links = JsonObject()
    links = JsonField()

class SalesOrderList(JsonObject):
    metadata = {
        'endpoint': 'sales_orders'
    }
    records = ObjectListField(SalesOrder)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()