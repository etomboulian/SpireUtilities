from .clients.companies import Companies
from requests.auth import HTTPBasicAuth

class ApiClient():
    def __init__(self, hostname, username, password, **kwargs):
        port = kwargs.get('port', 10880)
        authentication = HTTPBasicAuth(username, password)
        self.connection_info = {'hostname': hostname, 'port': port, 'authentication': authentication}

    # Gets a listing of the companies and the attached data
    @property
    def Companies(self):
        return Companies(self.connection_info)

    # Gets the Company object that was passed in as the company Name
    def Company(self, company_name):
        self.company = ApiClient.CompanyClient(company_name, self.connection_info)
        return self.company

    # Company Object
    class CompanyClient:
        def __init__(self, company_name, connection_info):
            self.company_name = company_name
            self.connection_info = connection_info
            from .clients.companies import Company as CompanyClient
            self.company = CompanyClient(self.company_name, self.connection_info)
        
        # get the company links
        @property
        def company_links(self):
            links = self.company.get()
            return links
        
        # get the current company name
        @property
        def name(self):
            return self.company_name

        # Get a Customers object on the current company
        @property
        def Customers(self):
            from .clients.customers import Customers
            return Customers(self.company_name, self.connection_info)
        
        # Get a Sales Orders Object on the current company
        @property
        def SalesOrders(self):
            from .clients.sales_orders import SalesOrders
            return SalesOrders(self.company_name, self.connection_info)