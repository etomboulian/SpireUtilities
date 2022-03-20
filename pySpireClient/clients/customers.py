from .api_client_base import ApiClientBase
import marshmallow_dataclass

class Customers(ApiClientBase):
    def __init__(self, company_name, connection_info, **kwargs):
        hostname = connection_info.get('hostname')
        authentication = connection_info.get('authentication')
        port = kwargs.get('port', 10880)
        super().__init__(hostname, authentication, port=port)
        self.url= self.root_url + 'companies/' + company_name + '/' + self.company_endpoints['customers']

    def list(self):
        response = super().list(self.url)
        from ..models.customer import CustomerList 
        customers_schema = marshmallow_dataclass.class_schema(CustomerList)()
        customers = customers_schema.load(response, partial=True)
        return customers.records
        