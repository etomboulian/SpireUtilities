import requests
from pykson import Pykson
from ..models.record_list import RecordList

class ApiClient:

    root_endpoints = {
        'status': 'status',
        'company_list': 'companies/'
    }

    company_endpoints = {
        'none': '',
        'customers': 'customers/',
        'sales_orders': 'sales/orders/'
    }

    def __init__(self, hostname, username, password, port=10880):
        self.session = requests.Session()
        self.session.auth = (username, password)
        self._company_name = None

        self.root_url = f'https://{hostname}:{port}/api/v2/'
        
    @property
    def company_name(self):
        return self._company_name
    
    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    def _validate(self, response):
        if response.status_code not in (200, 204):
            raise Exception(f"Response Code: {response.status_code}, {response.text}")

    def get(self, type, id=None, **kwargs):
        # if we have a company name then we have a selected company, if not then we get endpoints off the base
        if self.company_name is None:
            url = self.root_url + self.root_endpoints[type.endpoint]
        else:
            url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[type.endpoint]

        # if we have provided an ID then we are getting a resource and not a collection, append the id to the url
        if id is not None:
            url = url + id

        params = {}
        
        filter = kwargs.get('filter', None)

        if filter is not None:
            params['filter'] = filter

        # if we have start and or limit use the passed in values
        params['start'] = kwargs.get('start', 0)
        params['limit'] = kwargs.get('limit', 10)

        response = self.session.get(url,params=params)
        self._validate(response)
        obj = Pykson().from_json(response.text, type, accept_unknown=True)
        return obj

    def list(self, type, **kwargs):
        where = kwargs.get('filter', None)
        records = self.get(type, filter=where).records
        # Move the returned data records into a custom List type
        results = RecordList()
        for item in records:
            results.append(item)
        return results

    def all(self, type):
        page_size = 100
        # List of all results
        results = RecordList()

        list = self.get(type, limit=page_size)
        total_records = list.count
        total_pages = (total_records//page_size) + 1

        # take all of the records from the first page
        for item in list.records:
            results.append(item)
        
        for pageNumber in range(1,total_pages):
            list = self.get(type, start=(pageNumber*page_size), limit=page_size)
            for item in list.records:
                results.append(item)

        return results

    def update(self, object):
        raise NotImplementedError()

    def create(self, object):
        raise NotImplementedError()

    def delete(self, id):
        raise NotImplementedError()

class ItemClient:
    def __init__(self, api_client, single_item_type, collection_type):
        self.api_client = api_client
        self.item_type_single = single_item_type
        self.collection_type = collection_type

    def get(self, id):
        return self.api_client.get(self.single_item_type, id)

    def list(self, where=None):
        return self.api_client.list(self.collection_type, filter=where)
        
    def all(self):
        return self.api_client.all(self.collection_type)
