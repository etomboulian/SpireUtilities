from pykson import JsonObject, ObjectListField, StringField, IntegerField

class Customer(JsonObject):
    endpoint = 'customers'
    customerNo = StringField()
    name = StringField()

class CustomerList(JsonObject):
    endpoint = 'customers'

    records = ObjectListField(Customer)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()