from pykson import JsonObject, StringField, IntegerField, ObjectField

class PhoneNumber(JsonObject):
    number = StringField()
    format = IntegerField()

class OrderContact(JsonObject):
    name = StringField()
    email = StringField()
    phone = ObjectField(PhoneNumber)
    fax = ObjectField(PhoneNumber)
