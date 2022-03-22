from pykson import (JsonObject, ObjectListField, StringField, IntegerField, 
                    BooleanField, FloatField, DateField, ObjectField, JsonField)

from spire.models.data.editable_object import EditableObject
from .contacts import OrderContact, PhoneNumber

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
    contacts = ObjectListField(OrderContact)
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
    receivableAccount = StringField()
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
    created = StringField()
    createdBy = StringField()
    modified = StringField()
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
