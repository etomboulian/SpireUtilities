from marshmallow import Schema
from marshmallow_dataclass import dataclass
from marshmallow_enum import EnumField

from typing import Optional, List

from .address import Address

@dataclass
class PaymentTerms:
    id: int
    code: str
    description: str
    daysBeforeDue: int
    daysAllowed: int
    discountRate: str
    applyDiscountToNet: bool
    applyDiscountToFreight: bool
    udf: Optional[dict]
    createdBy: str
    modifiedBy: str
    created: str
    modified: str

@dataclass
class Customer:
    id: Optional[int]
    code: str
    customerNo: str
    name: str
    foregroundColor: int
    backgroundColor: int
    hold: bool
    status: str 
    reference: Optional[str]
    address: Address
    shippingAddresses: List[dict]
    paymentTerms: Optional[PaymentTerms]
    applyFinanceCharges: bool
    creditType: int
    creditLimit: float
    creditBalance: float
    creditApprovedBy: str
    creditApprovedDate: str
    currency: str
    userDef1: str
    userDef2: str
    discount: str
    receivableAccount: str
    defaultShipTo: str
    specialCode: str
    upload: bool
    lastModified: str
    paymentProviderId: Optional[int]
    udf: Optional[dict]
    createdBy: str
    modifiedBy: str
    created: str
    modified: str
    links: dict
    