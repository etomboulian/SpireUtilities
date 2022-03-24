from spire.api_client import ApiClient, ItemClient
from spire.models import Customer
from .models import CompanyList, CompanyLinks

class Companies:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client
    
    def list(self):
        return ItemClient(self.api_client, Company, CompanyList).list()

class Company:
    def __init__(self, api_client: str, company_name: str):
        self.api_client = api_client
        self.company_name = company_name
        self.api_client.company_name = company_name
        self.check_company_exists(company_name)

    def check_company_exists(self, company_name: str):
        data = self.info()
        if not hasattr(data, 'links'):
            raise Exception('Unable to instantiate Company Object. The selected company does not exist')

    # Get the data returned by the company endpoint
    def info(self):
        return self.api_client.get(CompanyLinks)

    @property
    def Addresses(self):
        from .models import AddressList
        return ItemClient(self.api_client, None, AddressList)

    @property
    def AccountsReceivable(self):
        from .models import ARTransaction, ARTransactionList
        return ItemClient(self.api_client, ARTransaction, ARTransactionList)

    @property
    def AccountsPayable(self):
        from .models import APTransaction, APTransactionList
        return ItemClient(self.api_client, APTransaction, APTransactionList)

    @property
    def Customers(self):
        from .models import Customer, CustomerList
        return ItemClient(self.api_client, Customer, CustomerList)

    @property
    def SalesOrders(self):
        from .models import SalesOrder, SalesOrderList 
        return ItemClient(self.api_client, SalesOrder, SalesOrderList)

    @property
    def SalesOrderItems(self):
        from .models import SalesOrderItemList
        return ItemClient(self.api_client, None, SalesOrderItemList)

    @property
    def SalesHistory(self):
        from .models import Invoice, InvoiceList
        return ItemClient(self.api_client, Invoice, InvoiceList)
    
    @property
    def SalesHistoryItems(self):
        from .models import InvoiceItemList
        return ItemClient(self.api_client, None, InvoiceItemList)