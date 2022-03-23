from typing import List
from pykson import JsonObject, JsonField, StringField, IntegerField, ObjectField, ObjectListField, DateTimeField, DateField, BooleanField

from spire.models.data.editable_object import EditableObject

class Number(JsonObject):
    number = StringField()
    format = IntegerField()

class Fax(JsonObject):
    number = StringField()
    format = IntegerField()

class Contact(JsonObject):
    name = StringField()
    email = StringField()
    phone: ObjectField(Number)
    fax: ObjectField(Fax)

class SalesTax(JsonObject):
    code = IntegerField()
    exempt = IntegerField()

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
    created = DateTimeField()
    modified = DateTimeField()
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
    rate = IntegerField()
    rateMethod = StringField(default_value='')
    glAccountNo = IntegerField()
    thousandsSeparator = StringField()
    lastYearRate = List[int]
    thisYearRate = List[int]
    nextYearRate = List[int]

class Customer(JsonObject):
    id = IntegerField()
    code = StringField()
    customerNo = StringField()
    name = StringField()

class Inventory:
    id = IntegerField()
    whse = StringField() 
    part_no = StringField()
    description = StringField()

class Serial:
    id = IntegerField()
    serial_number = IntegerField()
    whse = StringField()
    partNo = StringField()
    committedQty = IntegerField()
    unitCost = StringField()
    sellPrice = StringField()
    expiryDate = DateField()

class Item:
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

class Links:
    notes = StringField()

class Tax:
    code = IntegerField()
    name = StringField()
    shortName = StringField()
    rate = IntegerField()
    exemptNo = StringField()
    total = IntegerField()

class Order(JsonObject, EditableObject):
    metadata = { 'endpoint': 'sales_orders'}
    id = IntegerField()
    orderNo = StringField(default_value='')
    division = StringField()
    location = StringField()
    profitCenter = StringField()
    invoiceNo = StringField()
    customer = ObjectField(Customer, default_value=Customer())
    creditApprovedAmount = IntegerField()
    creditApprovedDate = DateField()
    creditApprovedUser = StringField()
    currency = ObjectField(Currency, default_value=Currency())
    status = StringField()
    type = StringField()
    hold = bool
    orderDate = DateField()
    invoiceDate = DateField()
    requiredDate = DateField()
    # recurrenceRule = None
    address = ObjectField(Address)
    shipping_address = ObjectField(Address, default_value=Address())
    contact = ObjectField(Contact, default_value=Contact())
    customerPo = StringField()
    batchNo = StringField()
    fob = StringField()
    incoterms = StringField()
    incoterms_place: StringField()
    reference_no: StringField()
    shipping_carrier: StringField()
    ship_date: StringField()
    tracking_no: StringField()
    terms_code: StringField()
    terms_text: StringField()
    freight: IntegerField()
    taxes: List[Tax]
    subtotal: StringField()
    subtotal_ordered: StringField()
    discount: IntegerField()
    total_discount: IntegerField()
    total: StringField()
    total_ordered: StringField()
    gross_profit: StringField()
    items = ObjectListField(Item)
    # payments = JsonField() 
    udf = JsonField()
    createdBy = StringField()
    modifiedBy = StringField()
    created = DateTimeField()
    modified = DateTimeField()
    deletedBy = StringField()
    deleted = DateTimeField()
    links = JsonObject(Links)