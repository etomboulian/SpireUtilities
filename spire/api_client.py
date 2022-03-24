import json
import requests
from pykson import Pykson
import logging
from .models.data.record_list import RecordList

logging.basicConfig(level=logging.INFO, filename='api_client.log')

class ApiClient:
    version = '0.0.1'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': f'Spire Python SDK v{version}'
        }
    proxies = {'http': 'http://127.0.0.1:8080'}

    # endpoints that are valid off the base_url
    root_endpoints = {
        'status': 'status',
        'company_list': 'companies/'
    }
    
    # endpoints that are valid off of the company_url
    company_endpoints = {
        'none': '',
        'customers': 'customers/',
        'addresses': 'addresses/',
        'ar_transactions': 'ar/transactions/',
        'sales_orders': 'sales/orders/',
        'sales_orders/items': 'sales/items/',
        'sales_history': 'sales/invoices/',
        'sales_history/items': 'sales/invoice_items'
    }

    def __init__(self, hostname, username, password, port=10880):
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update(self.headers)
        self._company_name = None

        self.root_url = f'http://{hostname}:{port}/api/v2/'
    
    # Provide a way to get and set the current company name
    @property
    def company_name(self):
        return self._company_name
    
    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    def get(self, type, id=None, **kwargs):
        # if we have a company name then we have a selected company, if not then we get endpoints off the base
        if self.company_name is None:
            url = self.root_url + self.root_endpoints[type.metadata['endpoint']]
        else:
            url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[type.metadata['endpoint']]

        # if we have provided an ID then we are getting a resource and not a collection, append the id to the url
        if id is not None:
            url = url + str(id)

        params = {}
        
        filter = kwargs.get('filter', None)

        if filter is not None:
            params['filter'] = filter

        # if we have start and or limit use the passed in values
        params['start'] = kwargs.get('start', 0)
        params['limit'] = kwargs.get('limit', 10)

        try:
            response = self.session.get(url,params=params, proxies=self.proxies)
            message = f'api_client.py:ApiClient.get {response.request.method} {response.request.url} {response.status_code}'
            logging.info(message)
        except Exception as e:
            logging.info(e)

        self._validate(response)
        obj = Pykson().from_json(response.text, type)
        return obj

    def list(self, type, **kwargs):
        where = kwargs.get('filter', None)
        records = self.get(type, filter=where).records
        # Move the returned data records into a custom List type
        results = RecordList()
        for item in records:
            item.metadata['api_client'] = self
            results.append(item)
        return results

    def all(self, type):
        page_size = 100
        results = RecordList()

        # Get the first page
        list = self.get(type, limit=page_size)
        total_records = list.count
        total_pages = (total_records//page_size) + 1

        # take all of the records into results list from the first page
        for item in list.records:
            item.metadata['api_client'] = self
            results.append(item)
        
        # get all remaining pages and extract the data into results list
        for pageNumber in range(1,total_pages):
            list = self.get(type, start=(pageNumber*page_size), limit=page_size)
            for item in list.records:
                results.append(item)

        # return the results list
        return results

    def save(self, obj):
        # if the object already has an id then try to update it
        if obj.id is not None:
            url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[obj.metadata['endpoint']] + str(obj.id)

            response = self.session.put(url, data=Pykson().to_json(obj), proxies=self.proxies)
            
            message = f'api_client.py:ApiClient.save: {response.request.method} {response.request.url} {response.status_code}'
            logging.info(message)

            self._validate(response)
            if response.status_code not in (200, 201):
                raise Exception("Unable to update the current object")

        # if the object has no id then create it
        else:
            url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[obj.metadata['endpoint']]

            data = Pykson().to_json(obj)
            data = self._strip_nulls(data)
            print(data)
            # Do the create
            response = self.session.post(url, data=data, proxies=self.proxies)
            
            message = f'api_client.py:ApiClient.save {response.request.method} {response.request.url} {response.status_code}'
            logging.info(message)

            self._validate(response)
            if response.status_code not in [201]:
                raise Exception("Unable to create the new object")

    def create(self, type, fields=None):
        if self.company_name is None:
            url = self.root_url + self.root_endpoints[type.metadata['endpoint']]
        else:
            url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[type.metadata['endpoint']]

        response = self.session.post(url, json=fields, proxies=self.proxies)
        message = f'api_client.py:ApiClient.create {response.request.method} {response.request.url} {response.status_code}'
        logging.info(message)
        
        self._validate(response)
        
        new_item_endpoint = response.headers['Location']
        print(new_item_endpoint)
        second_response = self.session.get(new_item_endpoint, proxies=self.proxies)
        self._validate(second_response)

        new_item = Pykson().from_json(second_response.text, type)
        return new_item

    def delete(self, obj):
        url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[obj.metadata['endpoint']] + str(obj.id)
        # Do Delete
        response = self.session.delete(url, data=Pykson().to_json(obj))
    
        message = f'api_client:ApiClient.delete {response.request.method} {response.request.url} {response.status_code}'
        logging.info(message)

        self._validate(response)
        if response.status_code not in [204]:
            raise Exception("Unable to delete the passed in object")

    # Validate that we received a response code indicating success
    @staticmethod
    def _validate(response):
        if response.status_code not in (200, 201, 204):
            message = f'''{response.request.method} {response.request.url} {response.status_code} {response.request.body} 
Response: {json.dumps(response.text)} '''
            logging.info(message)
            raise Exception(f"Response Code: {response.status_code}, {response.text}")

    @staticmethod
    def _strip_nulls(d):        
        d = json.loads(d)
        result = ApiClient._remove_empty_elements(d)
        s = json.dumps(result)
        return s

    @staticmethod
    def _remove_empty_elements(d):
        def empty(x):
            return x is None or x == {} or x == []
            
        if not isinstance(d, (dict, list)):
            return d
        elif isinstance(d, list):
            return [v for v in (ApiClient._remove_empty_elements(v) for v in d) if not empty(v)]
        else:
            return {k: v for k, v in ((k, ApiClient._remove_empty_elements(v)) for k, v in d.items()) if not empty(v)}

# Wrapper class around ApiClient to manage the single and collection item types
class ItemClient:
    def __init__(self, api_client, single_type, collection_type):
        self.api_client = api_client
        self.single_type = single_type
        self.collection_type = collection_type

    def get(self, id):
        if self.single_type is None:
            raise Exception("Unable to get an item that doesn't have a single item endpoint")
        item = self.api_client.get(self.single_type, id)
        item.metadata['api_client'] = self.api_client
        return item

    def list(self, where=None):
        if self.collection_type is None:
            raise Exception("Unable to list an item that doesn't have a collection endpoint")
        return self.api_client.list(self.collection_type, filter=where)
        
    def all(self):
        if self.collection_type is None:
            raise Exception("Unable to list an item that doesn't have a collection endpoint")
        return self.api_client.all(self.collection_type)

    def new(self, fields:dict=None):
        if self.single_type is None:
            raise Exception("Unable to create an item that doesn't have a single item endpoint")
        if fields is None:
            raise Exception("Unable to create a new item without the minimum required data")
        if not isinstance(fields, dict):
            raise Exception("Unable to create a new item, the required fields were not passed in as a dict")

        new_item = self.api_client.create(self.single_type, fields)
        new_item.metadata['api_client'] = self.api_client
        return new_item
    
    @staticmethod
    def check_min_required_fields(type, fields: dict):
        min_required_fields = set(type.metadata['min_required_fields'])
        print(min_required_fields)
        actual_fields = set(fields.keys())
        print(actual_fields)
        if not actual_fields.issuperset(min_required_fields):
            raise Exception(f'Minimum required fields were not given, unable to create a new instance of {type}')