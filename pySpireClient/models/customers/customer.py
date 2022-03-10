from ...models import Model

class Customer(Model):
    endpoint = 'customers'
    
    def __init__(self, customerNo: str, name: str = None):
        self.customerNo = customerNo
        self.name = name