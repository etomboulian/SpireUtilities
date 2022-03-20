from pykson import Pykson
from ..models import CompanyList, CompanyLinks

class Companies:
    def __init__(self, api_client):
        self.api_client = api_client

    def list(self):
        url = self.api_client.root_url + self.api_client.root_endpoints['company_list']
        response = self.api_client.session.get(url)
        company_list = Pykson().from_json(response.text, CompanyList)
        return company_list.records


class Company:
    def __init__(self, api_client, company_name):
        self.api_client = api_client
        self.company_name = company_name
        self.api_client.company_name = company_name
        
    def info(self):
        company_links = self.api_client.get(CompanyLinks)
        return company_links

    @property
    def SalesOrders(self):
        from .sales_orders import SalesOrders
        return SalesOrders(self.api_client)

    @property
    def Customers(self):
        from .customers import Customers
        return Customers(self.api_client)