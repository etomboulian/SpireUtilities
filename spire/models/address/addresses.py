from pykson import JsonObject, IntegerField, StringField

class OrderAddress(JsonObject):
    id = IntegerField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    provState = StringField()
    postalCode = StringField()
    country = StringField()

class OrderShippingAddress(JsonObject):
    id = IntegerField()
    shipId = StringField()
    name = StringField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    provState = StringField()
    postalCode = StringField()
    country = StringField()
    shipCode = StringField()
    shipDescription = StringField()