from pykson import (JsonObject, ObjectListField, StringField, IntegerField, DateTimeField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

from spire.data.editable_object import EditableObject

# /api/v2/companies/inspire2021/customers/
# Allows: [GET, HEAD, OPTIONS, POST]

class PhoneNumber(JsonObject):
    number = StringField()
    format = IntegerField()

class CustomerAddressContact(JsonObject):
    name = StringField()

class CustomerAddressTerritory(JsonObject):
    code = StringField()
    description = StringField()

class CustomerAddressSalesPerson(JsonObject):
    code = StringField()
    name = StringField()

class CustomerAddressSalesTaxes(JsonObject):
    code = IntegerField()
    exempt = StringField()

class CustomerAddress(JsonObject):
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
    contacts = ObjectListField(CustomerAddressContact)
    territory = ObjectField(CustomerAddressTerritory)
    salesperson = ObjectField(CustomerAddressSalesPerson)
    salesTaxes = ObjectListField(CustomerAddressSalesTaxes)
    shipCode = StringField()
    shipDescription = StringField()
    sellLevel = IntegerField()
    email = StringField()
    defaultWarehouse = StringField()

class PaymentTerms(JsonObject):
    code = StringField()
    description = StringField()

# /customers/ 
class Customer(JsonObject, EditableObject):
    metadata = {
        'endpoint':'customers'
    }
    id = IntegerField()
    customerNo = StringField()
    name = StringField()
    hold = BooleanField()
    status = StringField()
    creditType = IntegerField()
    creditLimit = FloatField(accepts_string=True)
    creditBalance = FloatField(accepts_string=True)
    creditApprovedBy = StringField()
    creditApprovedDate = DateField()
    openOrders = FloatField(accepts_string=True)
    lastInvoiceDate = DateField()
    specialCode = StringField()
    lastYearSales = FloatField(accepts_string=True)
    thisYearSales = FloatField(accepts_string=True)
    nextYearSales = FloatField(accepts_string=True)
    lastYearGP = FloatField(accepts_string=True)
    thisYearGP = FloatField(accepts_string=True)
    nextYearGP = FloatField(accepts_string=True)
    currency = StringField()
    userDef1 = StringField()
    userDef2 = StringField()
    invoiceType = StringField()
    statementType = StringField()
    applyFinanceCharges = BooleanField()
    averageDaysToPay = FloatField(accepts_string=True)
    lastPaymentAmt = FloatField(accepts_string=True)
    lastPaymentDate = DateField()
    reference = StringField()
    poRequired = BooleanField()
    paymentTerms = ObjectField(PaymentTerms)
    foregroundColor = IntegerField()
    backgroundColor = IntegerField()
    discount = FloatField(accepts_string=True)
    receivableAccount = StringField()
    defaultShipTo = StringField()
    upload = BooleanField()
    lastModified = StringField()
    address = ObjectField(CustomerAddress)
    created = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    createdBy = StringField()
    modified = DateTimeField(datetime_format='%Y-%m-%dT%H:%M:%S.%f')
    modifiedBy = StringField()
    links = JsonField()

    def __str__(self):
        return f'id: {self.id}, customerNo: {self.customerNo}, name: {self.name}, hold: {self.hold}'

# /customers/
class CustomerList(JsonObject):
    metadata = {
        'endpoint': 'customers'
    }
    records = ObjectListField(Customer)
    count = IntegerField()
    start = IntegerField()
    limit = IntegerField()
