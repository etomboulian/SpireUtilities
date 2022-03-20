from operator import truediv
from marshmallow_dataclass import dataclass
from typing import List, Optional

@dataclass
class BackupSchedule:
    next_backup: str
    last_success: str
    interval: str
    keep: int

@dataclass
class Company:
    name: Optional[str]
    description: Optional[str]
    needs_upgrade: Optional[bool]
    valid: Optional[bool]
    url: Optional[str]
    locations: Optional[dict]
    backup_schedules: List[dict]

@dataclass
class CompanyLinks:
    links: Optional[dict]
    name: Optional[str]
    description: Optional[str]
    needs_upgrade: bool
    url: Optional[str]


@dataclass
class CompanyList:
    records: Optional[List[Company]]
