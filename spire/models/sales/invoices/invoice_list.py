from pykson import JsonObject, ObjectListField, IntegerField, StringField, DateField, ObjectField, FloatField, JsonField, DateTimeField
from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/sales/invoices/
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
    foregroundColor = IntegerField()
    backgroundColor = IntegerField()

class Invoice(JsonObject, EditableObject):
    metadata = { 
        'endpoint': 'sales_history', 
        'allowed_methods': ['GET', 'POST']
        }
    id = IntegerField()
    invoiceNo = StringField()
    invoiceDate = DateField()
    customer = ObjectField(Customer)
    orderNo = StringField()
    orderDate = DateField()
    total = FloatField(accepts_string=True)
    baseTotal = FloatField()
    grossProfit = FloatField()
    grossProfitMargin = FloatField()
    transNo = StringField()
    division = StringField()
    location = StringField()
    profitCenter = StringField()
    fob = StringField()
    incoterms = StringField()
    incotermsPlace = StringField()
    referenceNo = StringField()
    discount = FloatField(accepts_string=True)
    totalDiscount = FloatField(accepts_string=True)
    totalCostAverage = FloatField(accepts_string=True)
    totalCostCurrent = FloatField(accepts_string=True)
    totalCostStandard = FloatField(accepts_string=True)
    termsCode = StringField()
    termsText = StringField()
    customerPO = StringField()
    salespersonNo = StringField()
    salespersonName = StringField()
    subTotal = FloatField(accepts_string=True)
    territoryCode = StringField()
    freight = FloatField(accepts_string=True)
    weight = FloatField(accepts_string=True)
    shipDate = DateField()
    shippingCarrier = StringField()
    trackingNo = StringField()
    requiredDate = DateField()
    wasQuoteNo = StringField()
    jobNo = StringField()
    jobAccountNo = StringField()
    invoicedUser = StringField()
    currency = StringField()
    address = ObjectField(OrderAddress)
    shippingAddress = ObjectField(OrderShippingAddress)
    contact = ObjectField(OrderContact)
    createdBy = StringField()
    modifiedBy = StringField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    links = JsonField()

class InvoiceList(JsonObject):
    records = ObjectListField(Invoice)
    start = IntegerField()
    limit = IntegerField()
    count = IntegerField()