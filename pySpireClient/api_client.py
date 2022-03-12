from .clients.companies import Companies
from requests.auth import HTTPBasicAuth

class ApiClient():

    def __init__(self, hostname, username, password, **kwargs):
        port = kwargs.get('port', 10880)
        authentication = HTTPBasicAuth(username, password)
        self.connection_info = {'hostname': hostname, 'port': port, 'authentication': authentication}

    @property
    def Companies(self):
        return Companies(self.connection_info['hostname'], self.connection_info['authentication'], port=self.connection_info['port'])

    class Company:
        def __init__(self, company_name):
            self.company_name = company_name

        @property
        def Customers(self):
            from .clients.customers import Customers
            return Customers(self.company_name, connection=self.connection_info)
        
        @property
        def SalesOrders(self):
            from .clients.sales_orders import SalesOrders
            return SalesOrders(self.company_name, connection=self.connection_info)
