from ..models import CustomerList
from ..models import Customer

class Customers:
    def __init__(self, api_client):
        self.api_client = api_client

    def list(self, where=None):
        return self.api_client.get(CustomerList, filter=where).records

    def all(self):
        page_size = 100
        # List of all results
        results = []

        list = self.api_client.get(CustomerList, limit=page_size)
        total_records = list.count
        total_pages = (total_records//page_size) + 1

        # take all of the records from the first page
        for customer in list.records:
            results.append(customer)
        
        for pageNumber in range(1,total_pages):
            list = self.api_client.get(CustomerList, start=(pageNumber*page_size), limit=page_size)
            for customer in list.records:
                results.append(customer)

        return results

    def get(self, id):
        return self.api_client.get(Customer, id)