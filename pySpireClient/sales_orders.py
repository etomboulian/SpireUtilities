from .api_client_base import ApiClientBase

class SalesOrders(ApiClientBase):
    def __init__(self, hostname, username, password, **kwargs):
        
        super().__init__(hostname, port, username, password)
        

