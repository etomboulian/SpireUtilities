from spire.clients.api_client import ApiClient, ItemClient
from ..models.companies import CompanyList, CompanyLinks

class Companies:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def list(self):
        return ItemClient(self.api_client, Company, CompanyList).list() #self.api_client.list(CompanyList)

class Company:
    def __init__(self, api_client: str, company_name: str):
        self.api_client = api_client
        self.company_name = company_name
        self.api_client.company_name = company_name
        
    def info(self):
        return self.api_client.get(CompanyLinks)

    @property
    def SalesOrders(self):
        from ..models.sales_orders import SalesOrder, SalesOrderList
        return ItemClient(self.api_client, SalesOrder, SalesOrderList)

    @property
    def Customers(self):
        from ..models.customers import Customer, CustomerList
        return ItemClient(self.api_client, Customer, CustomerList)
        