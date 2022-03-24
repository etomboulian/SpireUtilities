import logging
from .api_client import ApiClient
from .models import Status

class Server:  
    supported_versions = ['3.6.10']

    def __init__(self, hostname, username, password, port=10880):
        self.api_client = ApiClient(hostname, username, password, port)
        self.authenticated = False

        if not self.login():
            raise Exception('Not Logged in')

    # check to see if we are logged in to the given server, 
    # and that we are using a supported version of Spire
    def login(self):
        status = self.api_client.get(Status)
        
        if status.version in self.supported_versions:
            self.version_string = status.version
            self.authenticated = True
            return True
        else:
            raise Exception(f'Login Successful but Version {status.version} detected is not in supported versions list')
    
    # Spire company list interface
    @property
    def Companies(self):
        from .company import Companies
        return Companies(self.api_client)

    # Spire Single Company interface
    def Company(self, company_name):
        from .company import Company
        return Company(self.api_client, company_name)
