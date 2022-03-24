from pykson import (JsonObject, ObjectListField, StringField, IntegerField, DateTimeField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

class Customer(JsonObject):
    id = IntegerField()
    code = StringField()
    customerNo = StringField()
    name = StringField()

class Tax(JsonObject):
    code = IntegerField()
    name = StringField()
    shortName = StringField()
    rate = IntegerField(accepts_string=True)
    total = IntegerField(accepts_string=True)

class ARTransaction(JsonObject):
    metadata = {
        'endpoint': 'ar_transactions'
    }
    id = IntegerField()
    customer =  ObjectField(Customer)
    date = DateField()
    transType = StringField()
    transNo = StringField()
    referenceNo = StringField()
    customerPO = StringField()
    debitAmt = FloatField(accepts_string=True)
    creditAmt = FloatField(accepts_string=True)
    balance = FloatField(accepts_string=True)
    termsCode = StringField()
    subtotal = FloatField(accepts_string=True)
    freight = FloatField(accepts_string=True)
    taxes = ObjectListField(Tax)
    paymentMethod = JsonField()
    total = FloatField(accepts_string=True)
    memo = StringField()