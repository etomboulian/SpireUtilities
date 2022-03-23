from pykson import (JsonObject, ObjectListField, StringField, IntegerField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)
from spire.models.data.editable_object import EditableObject

class PhoneNumber(JsonObject):
    number = StringField()
    format = IntegerField()

class CustomerDetailPaymentTerms(JsonObject):
    id = IntegerField()
    code = StringField()
    description = StringField()
    daysBeforeDue = IntegerField()
    daysAllowed = IntegerField()
    discountRate = FloatField(accepts_string=True)
    applyDiscountToNet = BooleanField()
    applyDiscountToFreight = BooleanField()
    udf = JsonField()
    createdBy = StringField()
    modifiedBy = StringField()
    created = StringField()
    modified = StringField()

class CustomerDetailContact(JsonObject):
    name = StringField()
    email = StringField()
    phone = ObjectField(PhoneNumber)
    fax = ObjectField(PhoneNumber)

class CustomerAddressSalesPerson(JsonObject):
    code = StringField()
    name = StringField()

class CustomerAddressTerritory(JsonObject):
    code = StringField()
    description = StringField()

class CustomerAddressSalesTaxes(JsonObject):
    code = IntegerField()
    exempt = StringField()

class CustomerDetailAddress(JsonObject):
    id  = IntegerField()
    type = StringField()
    linkTable = StringField()
    linkType = StringField()
    linkNo = StringField()
    shipId = StringField()
    name = StringField()
    line1 = StringField()
    line2 = StringField()
    line3 = StringField()
    line4 = StringField()
    city = StringField()
    postalCode = StringField()
    provState = StringField()
    country = StringField()
    phone = ObjectField(PhoneNumber)
    fax = ObjectField(PhoneNumber)
    email = StringField()
    website = StringField()
    shipCode = StringField()
    shipDescription = StringField()
    salesperson = ObjectField(CustomerAddressSalesPerson)
    territory = ObjectField(CustomerAddressTerritory)
    sellLevel = IntegerField()
    glAccount = StringField()
    defaultWarehouse = StringField()
    udf = JsonField()
    created = StringField()
    modified = StringField()
    contacts = ObjectListField(CustomerDetailContact)
    salesTaxes = ObjectListField(CustomerAddressSalesTaxes)


# /customers/{id}
class CustomerDetail(JsonObject, EditableObject):
    metadata = {
        'endpoint':'customers'
    }
    id = IntegerField()
    code = StringField()
    customerNo = StringField()
    name = StringField()
    hold = BooleanField()
    status = StringField()
    reference = StringField()
    address = ObjectField(CustomerDetailAddress)
    created = StringField()
    modified = StringField()
    contacts = ObjectListField(CustomerDetailContact)
    salesTaxes = ObjectListField(CustomerAddressSalesTaxes)
    shippingAddresses = ObjectListField(CustomerDetailAddress)
    paymentTerms = ObjectField(CustomerDetailPaymentTerms)
    applyFinanceCharges = BooleanField()
    foregroundColor = IntegerField()
    backgroundColor = IntegerField()
    creditType = IntegerField()
    creditLimit = FloatField(accepts_string=True)
    creditBalance = FloatField(accepts_string=True)
    creditApprovedBy = StringField()
    creditApprovedDate = DateField()
    currency = StringField()
    userDef1 = StringField()
    userDef2 = StringField()
    discount = FloatField(accepts_string=True)
    receivableAccount = StringField(default_value="")
    defaultShipTo = StringField()
    specialCode = StringField()
    upload = BooleanField()
    lastModified = StringField()
    paymentProviderId = IntegerField()
    udf = JsonField()
    createdBy = StringField()
    modifiedBy = StringField()
    created = StringField()
    modified = StringField() 
    links = JsonField()