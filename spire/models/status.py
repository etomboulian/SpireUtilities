from pykson import JsonObject, StringField

class Status(JsonObject):
    endpoint = 'status'
    version = StringField()