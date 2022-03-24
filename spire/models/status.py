from pykson import JsonObject, StringField

# /api/v2/status
# Allows: [GET, HEAD, OPTIONS]

class Status(JsonObject):
    metadata = {
        'endpoint': 'status'
    }

    version = StringField()