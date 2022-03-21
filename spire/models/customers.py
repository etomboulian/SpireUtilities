from pykson import JsonObject, ObjectListField, StringField, IntegerField, BooleanField

from spire.models.editable import Editable

class Customer(JsonObject, Editable):
    metadata = {
        'endpoint':'customers'
    }
    
    id = IntegerField()
    customerNo = StringField()
    name = StringField()
    hold = BooleanField()    

    def __str__(self):
        return f'id: {self.id}, customerNo: {self.customerNo}, name: {self.name}, hold: {self.hold}'

    def _validate_content(self):
        # Here we should figure out if we have all of the required fields in order to save the object
        return True

class CustomerList(JsonObject):
    metadata = {
        'endpoint': 'customers'
    }
    records = ObjectListField(Customer)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()
