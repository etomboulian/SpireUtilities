from sqlite3 import Date
from tokenize import String
from pykson import JsonField, JsonObject, ObjectField, ObjectListField, IntegerField, StringField, BooleanField, FloatField, DateField, DateTimeField, ListField
from spire.models.data.editable_object import EditableObject
from typing import List

class Customer(JsonObject):
    customerNo = StringField()
    name = StringField()
    userDef2 = StringField()
    foregroundColor = IntegerField()
    backgroundColor = IntegerField()

class ShippingAddress(JsonObject):
    id = StringField()
    name = StringField()
    province = StringField()

class Invoice(JsonObject):
    id = IntegerField()
    territoryCode = StringField()
    salespersonNo = StringField()
    salespersonName = StringField()
    customerPO = StringField()
    shipDate = DateField()
    customer = ObjectField(Customer)
    shippingAddress = ObjectField(ShippingAddress)
    currency = StringField()

class InvoiceItem(JsonObject):
    metadata = {
        'endpoint': 'sales_history/items'
    }
    id = IntegerField()
    invoiceNo = StringField()
    recNo = IntegerField()
    whse = StringField()
    partNo = StringField()
    itemType = IntegerField()
    description = StringField()
    invoiceDate = DateField()
    orderQty = IntegerField(accepts_string=True)
    committedQty = IntegerField(accepts_string=True)
    backorderQty = IntegerField(accepts_string=True)
    unitPrice = FloatField(accepts_string=True)
    extendedPrice = FloatField(accepts_string=True)
    sellMeasure = StringField()
    taxApplicable = ListField(bool)
    averageCost = FloatField(accepts_string=True)
    averageMargin = FloatField(accepts_string=True)
    currentCost = FloatField(accepts_string=True)
    currentMargin = FloatField(accepts_string=True)
    standardCost = FloatField(accepts_string=True)
    standardMargin = FloatField(accepts_string=True)
    lineDiscountPct = FloatField(accepts_string=True)
    discountPct = FloatField(accepts_string=True)
    inventoryGroupNo = StringField()
    requiredDate = DateField()
    invoice = ObjectField(Invoice)
    employeeNo = StringField()
    promoCode = StringField()
    inventoryGL = StringField()
    revenueGL = StringField()
    costGL = StringField()
    refNo = StringField()
    upcCode = StringField()
    levyCode = StringField()
    jobNo = StringField()
    jobAccountNo = StringField()
    comment = StringField()
    weight = FloatField(accepts_string=True)

class InvoiceItemList(JsonObject):
    metadata = {
        'endpoint': 'sales_history/items'
    }
    records = ObjectListField(InvoiceItem)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()