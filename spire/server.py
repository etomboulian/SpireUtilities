from .clients.api_client import ApiClient
from .models import Status

class Server:
    
    supported_versions = ['3.6.10']

    def __init__(self, hostname, username, password, port=10880):
        self.api_client = ApiClient(hostname, username, password, port)
        self.authenticated = False

        if not self.login():
            raise Exception('Not Logged in')

    def login(self):
        status = self.api_client.get(Status)
        
        if status.version in self.supported_versions:
            self.version_string = status.version
            self.authenticated = True
            return True
        else:
            raise Exception(f'Login Successful but Version {status.version} detected is not in supported versions list')

    @property
    def Companies(self):
        from .clients.companies import Companies
        return Companies(self.api_client)

    def Company(self, company_name):
        from .clients.companies import Company
        return Company(self.api_client, company_name)
