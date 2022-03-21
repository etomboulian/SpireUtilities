from pykson import JsonObject, StringField

class Status(JsonObject):
    metadata = {
        'endpoint': 'status'
    }

    version = StringField()