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
    name: Optional[str]
    email: Optional[str]
    phone: Optional[PhoneNumber]
    fax: Optional[FaxNumber]

@dataclass
class SalesTax:
    code: int
    exempt: str

@dataclass
class Address:
    id: Optional[int]
    type: Optional[str]
    linkTable: Optional[str]
    linkType: Optional[str]
    linkNo: Optional[str]
    shipId: Optional[str]
    name: Optional[str]
    line1: Optional[str]
    line2: Optional[str]
    line3: Optional[str]
    line4: Optional[str]
    city: Optional[str]
    postalCode: Optional[str]
    provState: Optional[str]
    country: Optional[str]
    phone: Optional[PhoneNumber]
    fax: Optional[FaxNumber]
    email: Optional[str]
    website: Optional[str]
    shipCode: Optional[str]
    shipDescription: Optional[str]
    salesperson: Optional[SalesPerson]
    territory: Optional[Territory]
    sellLevel: Optional[int]
    glAccount: Optional[str]
    defaultWarehouse: Optional[str]
    udf: Optional[dict]
    created: Optional[str]
    modified: Optional[str]
    contacts: Optional[List[Contact]]
    salesTaxes: Optional[List[dict]]
