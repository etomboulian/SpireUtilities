import requests
from .api_client_base import ApiClientBase
from ..models.company import CompanyList
import marshmallow_dataclass

class Companies(ApiClientBase):
    def __init__(self, hostname, authentication, **kwargs):
        port = kwargs.get('port', 10880)
        super().__init__(hostname, authentication, port=port)
        
        self.type = 'companies'
        self.base_url = self.root_url
        self.endpoint = self.root_endpoints[self.type]

    def list(self):
        url = self.base_url + self.endpoint + '?limit=0'

        response = requests.get(url, auth=self.auth, headers=self.headers)
        raw_response = response.json()

        company_list_schema = marshmallow_dataclass.class_schema(CompanyList)()
        companies = company_list_schema.load(raw_response)
        return companies.records