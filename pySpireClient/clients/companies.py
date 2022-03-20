from .api_client_base import ApiClientBase
from ..models.company import Company, CompanyLinks, CompanyList
import marshmallow_dataclass

class Company(ApiClientBase):
    def __init__(self, company_name, connection_info, **kwargs):
        hostname = connection_info.get('hostname')
        authentication = connection_info.get('authentication')
        port = kwargs.get('port', 10880)
        super().__init__(hostname, authentication, port=port)
        self.url= self.root_url + 'companies/' + company_name + '/'
        self.company = self.get()

    def get(self):
        response = super().get(self.url)
        company_links_schema = marshmallow_dataclass.class_schema(CompanyLinks)()
        company_links = company_links_schema.load(response)
        return company_links

class Companies(ApiClientBase):
    def __init__(self, connection_info, **kwargs):
        hostname = connection_info.get('hostname')
        authentication = connection_info.get('authentication')
        port = kwargs.get('port', 10880)
        super().__init__(hostname, authentication, port=port)
        self.url = self.root_url + self.root_endpoints['companies']

    def list(self):
        url = self.url
        params = {'limit': '0'}
        response = super().list(url, params=params)
        
        company_list_schema = marshmallow_dataclass.class_schema(CompanyList)()
        companies = company_list_schema.load(response)

        return companies.records

    def get(self, company_name):
        url = self.url + str(company_name)
        response = super().get(url)
        
        company_schema = marshmallow_dataclass.class_schema(CompanyLinks)
        company_links = company_schema.load(response)

        return company_links