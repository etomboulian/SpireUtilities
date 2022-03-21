from pykson import JsonObject, ObjectListField, StringField, IntegerField, BooleanField

from spire.models.editable import Editable

class Customer(JsonObject, Editable):
    metadata = {
        'endpoint':'customers',
        'in_edit': None,
        'api_client': None
    }
    
    id = IntegerField()
    customerNo = StringField()
    name = StringField()
    hold = BooleanField()    

class CustomerList(JsonObject):
    metadata = {
        'endpoint': 'customers'
    }
    records = ObjectListField(Customer)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()
