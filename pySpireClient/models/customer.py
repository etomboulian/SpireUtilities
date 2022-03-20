from datetime import date, datetime
from email.policy import default
from marshmallow_dataclass import dataclass
from typing import Optional, List
from .address import Address

@dataclass
class PaymentTerms:
    id: Optional[int]
    code: Optional[str]
    description: Optional[str]
    daysBeforeDue: Optional[int]
    daysAllowed: Optional[int]
    discountRate: Optional[str]
    applyDiscountToNet: Optional[bool]
    applyDiscountToFreight: Optional[bool]
    udf: Optional[dict]
    createdBy: Optional[str]
    modifiedBy: Optional[str]
    created: Optional[str]
    modified: Optional[str]

@dataclass
class Customer:
    id: Optional[int]
    customerNo: str
    name: Optional[str]
    hold: bool
    status: str
    creditType: int
    creditLimit: float
    creditBalance: float
    creditApprovedBy: str
    creditApprovedDate: str
    openOrders: Optional[str]
    lastInvoiceDate : Optional[str]
    specialCode: Optional[str]
    lastYearSales: Optional[float]
    thisYearSales: Optional[float]
    nextYearSales: Optional[float]
    lastYearGP: float
    thisYearGP: float
    nextYearGP: float
    currency: Optional[str]
    userDef1: Optional[str]
    userDef2: Optional[str]
    invoiceType: str
    statementType: str
    applyFinanceCharges: bool
    averageDaysToPay: float
    #lastPaymentAmt: float
    lastPaymentDate: Optional[date]
    reference: Optional[str]
    poRequired: bool
    paymentTerms: Optional[PaymentTerms]
    foregroundColor: Optional[int]
    backgroundColor: Optional[int]
    discount: float
    receivableAccount: str
    defaultShipTo: Optional[str]
    upload: bool
    lastModified: datetime
    address: Optional[Address]
    salesTaxAssociation: Optional[dict]
    created: str
    createdBy: str
    modified: str
    modifiedBy: str
    links: dict

@dataclass
class CustomerList:
    records: Optional[List[Customer]]
    start: Optional[int]
    limit: Optional[int]
    count: Optional[int]

class SalesOrderCustomer:
    pass