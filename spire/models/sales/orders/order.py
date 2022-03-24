from typing import List
from pykson import JsonObject, JsonField, StringField, IntegerField, ObjectField, ObjectListField, DateTimeField, DateField, BooleanField, ListField, FloatField

from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/sales/orders/{id}
# Allows: [GET, HEAD, PUT, DELETE, OPTIONS]

class Number(JsonObject):
    number = StringField()
    format = IntegerField()

class Fax(JsonObject):
    number = StringField()
    format = IntegerField()

class Contact(JsonObject):
    name = StringField()
    email = StringField()
    phone = ObjectField(Number)
    fax = ObjectField(Fax)

class SalesTax(JsonObject):
    code = IntegerField()
    exempt = StringField()

class Salesperson(JsonObject):
    code = StringField()
    name = StringField()

class Territory(JsonObject):
    code = StringField()
    description = StringField()

class Address(JsonObject):
    id = IntegerField()
    type = StringField()
    linkTable = StringField()
    linkType = StringField()
    linkNo = StringField()
    shipId = StringField()
    name = StringField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    postalCode = StringField()
    provState = StringField()
    country = StringField()
    phone = ObjectField(Number)
    fax = ObjectField(Fax)
    email = StringField()
    website = StringField()
    shipCode = StringField()
    shipDescription = StringField()
    salesperson = ObjectField(Salesperson)
    territory = ObjectField(Territory)
    sellLevel = IntegerField()
    glAccount = StringField()
    defaultWarehouse = StringField()
    udf = JsonField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    contacts = ObjectListField(Contact)
    salesTaxes = ObjectListField(SalesTax)

class Currency(JsonObject):
    id = IntegerField()
    code = StringField()
    description = StringField()
    country = StringField()
    units = StringField()
    fraction = StringField()
    symbol = StringField()
    decimalPlaces = IntegerField()
    symbolPosition = StringField()
    rate = IntegerField(accepts_string=True)
    rateMethod = StringField()
    glAccountNo = StringField()
    thousandsSeparator = StringField()
    lastYearRate = ListField(str)
    thisYearRate = ListField(str)
    nextYearRate = ListField(str)

class Customer(JsonObject):
    id = IntegerField()
    code = StringField()
    customerNo = StringField()
    name = StringField()

class Inventory(JsonObject):
    id = IntegerField()
    whse = StringField() 
    part_no = StringField()
    description = StringField()

class Serial(JsonObject):
    id = IntegerField()
    serial_number = IntegerField()
    whse = StringField()
    partNo = StringField()
    committedQty = IntegerField()
    unitCost = StringField()
    sellPrice = StringField()
    expiryDate = DateField()

class Item(JsonObject):
    id = IntegerField()
    orderNo = StringField()
    sequence = IntegerField()
    parentSequence = IntegerField()
    inventory = ObjectField(Inventory)
    serials = ObjectListField(Serial)
    whse = StringField()
    partNo = StringField()
    description = StringField()
    comment = StringField()
    orderQty = IntegerField()
    committedQty = IntegerField()
    backorderQty = IntegerField()
    sellMeasure = StringField()
    retailPrice = StringField()
    unitPrice = StringField()
    userPrice = bool
    discountable = bool
    discountPct = IntegerField()
    discountAmt = IntegerField()
    taxFlags = List[bool]
    vendor = StringField()
    levyCode = IntegerField()
    requiredDate = DateField()
    extendedPriceOrdered = StringField()
    extendedPriceCommitted = StringField()
    kit = BooleanField()
    suppress = BooleanField()
    udf = JsonField()

class Tax(JsonObject):
    code = IntegerField()
    name = StringField()
    shortName = StringField()
    rate = FloatField(accepts_string=True)
    exemptNo = StringField()
    total = FloatField(accepts_string=True)

class Order(JsonObject, EditableObject):
    metadata = { 
        'endpoint': 'sales_orders', 
        'allowed_methods': ['GET', 'PUT', 'DELETE'],
        'min_required_fields': {'customer': ['customerNo']}
        }
    id = IntegerField()
    orderNo = StringField()
    division = StringField()
    location = StringField()
    profitCenter = StringField()
    invoiceNo = StringField()
    customer = ObjectField(Customer, default_value=Customer())
    creditApprovedAmount = FloatField(accepts_string=True)
    creditApprovedDate = DateField()
    creditApprovedUser = StringField()
    currency = ObjectField(Currency, default_value=Currency())
    status = StringField()
    type = StringField()
    hold = BooleanField()
    orderDate = DateField()
    invoiceDate = DateField()
    requiredDate = DateField()
    recurrenceRule = StringField()
    address = ObjectField(Address)
    shippingAddress = ObjectField(Address, default_value=Address())
    contact = ObjectField(Contact, default_value=Contact())
    customerPO = StringField()
    batchNo = StringField()
    fob = StringField()
    incoterms = StringField()
    incotermsPlace = StringField()
    referenceNo = StringField()
    shippingCarrier = StringField()
    shipDate = StringField()
    trackingNo = StringField()
    termsCode = StringField()
    termsText = StringField()
    freight = FloatField(accepts_string=True)
    taxes = ObjectListField(Tax)
    subtotal = FloatField(accepts_string=True)
    subtotalOrdered = FloatField(accepts_string=True)
    discount = FloatField(accepts_string=True)
    totalDiscount = FloatField(accepts_string=True)
    total = FloatField(accepts_string=True)
    totalOrdered = FloatField(accepts_string=True)
    grossProfit = FloatField(accepts_string=True)
    items = ObjectListField(Item)
    payments = ListField(str) 
    udf = JsonField()
    createdBy = StringField()
    modifiedBy = StringField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    deletedBy = StringField()
    deleted = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    links = JsonField()