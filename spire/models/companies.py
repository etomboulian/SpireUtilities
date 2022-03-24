from pykson import JsonObject, ObjectListField, StringField, BooleanField, IntegerField, JsonField

class BackupSchedule(JsonObject):
    next_backup = StringField()
    last_success = StringField()
    interval = StringField()
    keep = IntegerField()

class Company(JsonObject):
    metadata = {
        'endpoint': 'none'
    }
    name = StringField()
    description = StringField()
    needs_upgrade = BooleanField()
    valid = BooleanField()
    url = StringField()
    locations = JsonField()
    backup_schedules = ObjectListField(BackupSchedule)

# /api/v2/companies/
# Allows: [GET, HEAD, OPTIONS]

class CompanyList(JsonObject):
    metadata = {
        'endpoint': 'company_list'
    }
    
    records = ObjectListField(Company)


# /api/v2/companies/{companyName}
# Allows: [GET, HEAD, PUT, DELETE, OPTIONS]

class CompanyLinks(JsonObject):
    metadata = {
        'endpoint': 'none'
    }

    links = JsonField()
    name = StringField()
    description = StringField()
    needs_upgrade = BooleanField()
    url = StringField()