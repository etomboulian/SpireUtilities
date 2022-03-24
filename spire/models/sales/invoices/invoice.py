from pykson import JsonObject, IntegerField, StringField, ObjectField, ObjectListField, DateField, JsonField, DateTimeField
from typing import List

from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/sales/invoices/{id}
# Allows: [GET, HEAD, PUT, DELETE, OPTIONS]

class PhoneFaxNumber(JsonObject):
    number = StringField()
    format = IntegerField()

class Contact(JsonObject):
    name = StringField()
    email = StringField()
    phone = ObjectField(PhoneFaxNumber, default_value=PhoneFaxNumber())
    fax = ObjectField(PhoneFaxNumber, default_value=PhoneFaxNumber())

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
    phone = ObjectField(PhoneFaxNumber, default_value=PhoneFaxNumber())
    fax = ObjectField(PhoneFaxNumber, default_value=PhoneFaxNumber())
    email = StringField()
    website = StringField()
    shipCode = StringField()
    shipDescription = StringField()
    salesperson = ObjectField(Salesperson, default_value=Salesperson())
    territory =  ObjectField(Territory, default_value=Territory())
    sellLevel = IntegerField()
    glAccount = IntegerField()
    defaultWarehouse = StringField()
    udf = JsonField()
    created = StringField()
    modified = StringField()
    contacts = ObjectListField(Contact)
    salesTaxes = ObjectListField(SalesTax)

class Currency:
    id = IntegerField()
    code = StringField()
    description = StringField()
    country = StringField()
    units = StringField()
    fraction = StringField()
    symbol = StringField()
    decimalPlaces = IntegerField()
    symbolPosition = StringField()
    rate = IntegerField()
    rateMethod = StringField()
    glAccountNo = IntegerField()
    thousandsSeparator = StringField()
    lastYearRate = List[int]
    thisYearRate = List[int]
    nextYearRate = List[int]

class Customer:
    id = IntegerField()
    code = StringField()
    customer_no = StringField()
    name = StringField()

class Inventory:
    id = IntegerField()
    whse = StringField()
    part_no = StringField()
    description = StringField()

class Item:
    id = IntegerField()
    invoiceNo = StringField()
    sequence = IntegerField()
    inventory = ObjectField(Inventory, default_value=Inventory())
    whse = StringField()
    partNo = StringField()
    description = StringField()
    comment = StringField()
    orderQty = IntegerField()
    committedQty = IntegerField()
    backorderQty = IntegerField()
    retailPrice = StringField()
    unitPrice = StringField()
    lineDiscountPct = IntegerField()
    discountPct = IntegerField()
    taxFlags: List[bool]
    sellMeasure = StringField()
    extendedPriceOrdered = StringField()
    extendedPriceCommitted = StringField()
    udf = JsonField()

class Links:
    notes = StringField()

class Tax:
    code = IntegerField()
    name = StringField()
    shortName = StringField()
    rate = IntegerField()
    exemptNo = StringField()
    total = StringField()

class Invoice(JsonObject, EditableObject):
    metadata = { 
        'endpoint': 'sales_history', 
        'allowed_methods': ['GET', 'PUT', 'DELETE']
        
        }
    id = IntegerField()
    invoiceNo = StringField()
    orderNo = StringField()
    division = StringField()
    location = StringField()
    profitCenter = StringField()
    customer = ObjectField(Customer, default_value=Customer())
    currency = ObjectField(Currency, default_value=Currency())
    orderDate = DateField()
    invoiceDate = DateField()
    requiredDate = DateField()
    address = ObjectField(Address, default_value=Address())
    shippingAddress = ObjectField(Address, default_value=Address())
    customerPo = StringField()
    fob = StringField()
    incoterms = StringField()
    incotermsPlace = StringField()
    referenceNo = StringField()
    shippingCarrier = StringField()
    shipDate = StringField()
    trackingNo = StringField()
    termsCode = StringField()
    termsText = StringField()
    freight = IntegerField()
    taxes: List[int]
    subtotal = StringField()
    total = StringField()
    items = ObjectListField(Item)
    payments = ObjectListField(JsonField())
    udf = JsonField()
    createdBy = StringField()
    modifiedBy = StringField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    links = ObjectField(Links)
