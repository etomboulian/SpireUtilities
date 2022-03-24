from pykson import (JsonObject, ObjectListField, StringField, IntegerField, DateTimeField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/ap/batches/
# Allows: [GET, HEAD, OPTIONS]

class APBatch(JsonObject, EditableObject):
    id = IntegerField()
    date = DateField()
    dueBy = DateField()
    currency = StringField()
    total = FloatField(accepts_string=True)
    paymentAccount = StringField()
    note = StringField()
    status = StringField()
    createdUser = StringField()

class APBatchList(JsonObject):
    metadata = {
        'endpoint': 'ap_batches'
    }
    records = ObjectListField(APBatch)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()