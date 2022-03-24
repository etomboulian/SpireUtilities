from pykson import (JsonObject, ObjectListField, StringField, IntegerField, DateTimeField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/ar/transactions/
# Allows: [GET, HEAD, OPTIONS, POST]

class Customer(JsonObject):
    id = IntegerField()
    code = StringField()

class Self(JsonObject):
    self = StringField()

class AccountsReceivable(JsonObject, EditableObject):
    metadata = {
        'endpoint': 'ar_transactions'
    }
    id = IntegerField()
    customer = ObjectField(Customer)
    date = DateField()
    linkDate = DateField() 
    transType = StringField()
    transNo = StringField()
    refNo = StringField()
    debitAmt = StringField()
    creditAmt = StringField()
    linkBalance = FloatField(accepts_string=True)
    user = StringField()
    termsCode = StringField()
    dueDate = DateField()
    referenceNo = StringField()
    customerPO = StringField()
    links = ObjectField(Self)

class ARTransactionList(JsonObject):
    metadata = {
        'endpoint': 'ar_transactions'
    }
    records = ObjectListField(AccountsReceivable)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()

