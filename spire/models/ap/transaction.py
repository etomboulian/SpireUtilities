from sqlite3 import Date
from pykson import (JsonObject, ObjectListField, StringField, IntegerField, DateTimeField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

from spire.models.data.editable_object import EditableObject

class Tax(JsonObject):
    code = IntegerField()
    name = IntegerField()
    shortName = StringField()
    rate = FloatField(accepts_string=True)
    total = FloatField(accepts_string=True)

class Vendor(JsonObject):
    id = IntegerField()
    vendorNo = StringField()
    code = StringField()
    name = StringField()

class APTransaction(JsonObject, EditableObject):
    metadata = {
        'endpoint': 'ap_transactions'
    }
    id = IntegerField()
    vendor = ObjectField(Vendor)
    date = DateField()
    transType = StringField()
    transNo = StringField()
    referenceNo = IntegerField()
    purchaseNo = StringField()
    debitAmt = FloatField(accepts_string=True)
    creditAmt = FloatField(accepts_string=True)
    balance = FloatField(accepts_string=True)
    termsCode = StringField()
    subtotal = StringField()
    freight = IntegerField()
    taxes = ObjectListField(Tax)
    total = FloatField(accepts_string=True)
    memo = StringField()
    expenseAccountNo = StringField()