from .companies import Companies
from requests.auth import HTTPBasicAuth

class ApiClient():

    def __init__(self, hostname, username, password, **kwargs):
        port = kwargs.get('port', 10880)
        authentication = HTTPBasicAuth(username, password)
        self.connection_info = {'hostname': hostname, 'port': port, 'authentication': authentication}

    def Companies(self):
        return Companies(self.connection_info['hostname'], self.connection_info['authentication'], port=self.connection_info['port'])