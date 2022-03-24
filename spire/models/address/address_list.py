from pykson import JsonField, JsonObject, ObjectField, ObjectListField, IntegerField, StringField, BooleanField, FloatField, DateField, DateTimeField, ListField

class Fax(JsonObject):
    number = StringField()
    format = IntegerField()

class Contact(JsonObject):
    name = StringField()
    phone = ObjectField(Fax)
    email = StringField()

class Salesperson(JsonObject):
    code = StringField()
    name = StringField()

class Territory(JsonObject):
    code = StringField()
    description = StringField()

class Address(JsonObject):
    metadata = {
        'endpoint': 'addresses'
    }
    id = IntegerField()
    recordType = StringField()
    linkType = StringField()
    linkNo = StringField()
    shipId = StringField()
    type = StringField()
    name = StringField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    postalCode = StringField()
    provState = StringField()
    country = StringField()
    phone = ObjectField(Fax)
    fax = ObjectField(Fax)
    contacts = ObjectListField(Contact)
    territory = ObjectField(Territory)
    salesperson = ObjectField(Salesperson)
    sellLevel = IntegerField(accepts_string=True)
    email = StringField()
    website = StringField()
    shipCode = StringField()
    shipDescription = StringField()
    glAccount = StringField()
    taxCodes = ListField(int)
    defaultWarehouse = StringField()
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    createdBy = StringField()
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modifiedBy = StringField()

class AddressList(JsonObject):
    metadata = {
        'endpoint': 'addresses'
    }
    records = ObjectListField(Address)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()