from pySpireClient.models.sales_order import SalesOrderList
from .api_client_base import ApiClientBase
import marshmallow_dataclass

class SalesOrders(ApiClientBase):
    def __init__(self, company_name, connection_info, **kwargs):
        hostname = connection_info.get('hostname')
        authentication = connection_info.get('authentication')
        port = kwargs.get('port', 10880)
        super().__init__(hostname, authentication, port=port)
        self.url= self.root_url + 'companies/' + company_name + '/' + self.company_endpoints['sales_orders']

    def list(self):
        response = super().list(self.url)
        from ..models.sales_order import SalesOrderList
        sales_orders_schema = marshmallow_dataclass.class_schema(SalesOrderList)()
        sales_orders = sales_orders_schema.load(response, partial=True)
        return sales_orders.records


