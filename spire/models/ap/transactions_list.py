from pykson import (JsonObject, ObjectListField, StringField, IntegerField, DateTimeField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

from spire.models.data.editable_object import EditableObject

class Links(JsonField):
    self = StringField()

class Vendor(JsonField):
    id = IntegerField()
    code = StringField()

class AccountsPayable(JsonField, EditableObject):
    id = IntegerField()
    vendor = ObjectField(Vendor)
    date = DateField()
    transType = StringField()
    transNo = StringField()
    referenceNo = IntegerField()
    purchaseNo = StringField()
    debitAmt = FloatField(accepts_string=True)
    creditAmt = FloatField(accepts_string=True)
    balance = IntegerField()
    user = StringField()
    termsCode = StringField()
    freight = IntegerField()
    links = ObjectField(Links)

class APTransactionList(JsonObject):
    metadata = {
        'endpoint': 'ap_transactions'
    }
    records = ObjectListField(AccountsPayable)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()