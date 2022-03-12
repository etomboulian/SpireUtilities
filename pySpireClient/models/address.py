from marshmallow_dataclass import dataclass
from typing import Optional, List

from dataclasses import field

@dataclass
class PhoneNumber:
    number: str
    format: Optional[int]

@dataclass
class FaxNumber:
    number: str
    format: Optional[int]

@dataclass
class SalesPerson:
    code: str
    name: str

@dataclass
class Territory:
    code: str
    description: str

@dataclass
class Contact:
    id: Optional[int]
    contact_type: Optional[dict]
    name: str
    email: str
    phone: PhoneNumber
    fax: FaxNumber

@dataclass
class SalesTax:
    code: int
    exempt: str

@dataclass
class Address:
    id: int
    type: str 
    linkTable: str 
    linkType: str 
    linkNo: str
    shipId: str
    name: str
    line1: str
    line2: str
    line3: str
    line4: str
    city: str
    postalCode: str
    provState: str 
    country: str 
    phone: PhoneNumber 
    fax: FaxNumber
    email: str
    website: str
    shipCode: str
    shipDescription: str
    salesperson: SalesPerson
    territory: Territory
    sellLevel: Optional[int]
    glAccount: str
    defaultWarehouse: str
    udf: Optional[dict]
    created: str
    modified: str
    contacts: List[Contact]
    salesTaxes: List[dict]