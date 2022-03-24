from pykson import (JsonObject, ObjectListField, StringField, IntegerField, DateTimeField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/ar/batches/
# Allows: [GET, HEAD, OPTIONS]

class ARBatch(JsonObject, EditableObject):
    id = IntegerField()
    date = DateField()
    dueBy = DateField()
    currency = StringField()
    total = FloatField(accepts_string=True)
    paymentAccount = StringField()
    note = StringField()
    status = StringField()
    createdUser = StringField()

class ARBatchList(JsonObject):
    metadata = {
        'endpoint': 'ar_batches'
    }
    records = ObjectListField(ARBatch)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()