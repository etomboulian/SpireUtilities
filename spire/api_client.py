import json
import requests
from pykson import Pykson
from .models.data.record_list import RecordList

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
        'sales_orders': 'sales/orders/'
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

    # Validate that we received a response code indicating success
    def _validate(self, response):
        if response.status_code not in (200, 201, 204):
            raise Exception(f"Response Code: {response.status_code}, {response.text}")

    def get(self, type, id=None, **kwargs):
        # if we have a company name then we have a selected company, if not then we get endpoints off the base
        if self.company_name is None:
            url = self.root_url + self.root_endpoints[type.endpoint]
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
            response = self.session.get(url,params=params)
        except Exception as e:
            raise e

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
        results = RecordList()

        list = self.get(type, limit=page_size)
        total_records = list.count
        total_pages = (total_records//page_size) + 1

        # take all of the records into results list from the first page
        for item in list.records:
            results.append(item)
        
        # get all remaining pages and extract the data into results list
        for pageNumber in range(1,total_pages):
            list = self.get(type, start=(pageNumber*page_size), limit=page_size)
            for item in list.records:
                results.append(item)

        # return the results list
        return results

    def save(self, obj):
        url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[obj.metadata['endpoint']] + str(obj.id)
        # clear the metadata dict before serialization
        # self._clear_metadata(obj)
        
        # Do the update using the object passed in
        response = self.session.put(url, data=Pykson().to_json(obj))
        self._validate(response)
        if response.status_code not in (200, 201):
            raise Exception("Unable to update the current object")


    def create(self, object):
        raise NotImplementedError()

    def delete(self, obj):
        url = self.root_url + self.root_endpoints['company_list'] + self.company_name + '/' + self.company_endpoints[obj.metadata['endpoint']] + str(obj.id)
        # self._clear_metadata(obj)
        response = self.session.delete(url, data=Pykson().to_json(obj))
        self._validate(response)
        if response.status_code not in (204):
            raise Exception("Unable to delete the passed in object")

# Wrapper class around ApiClient to manage the single and collection item types
class ItemClient:
    def __init__(self, api_client, single_type, collection_type):
        self.api_client = api_client
        self.single_type = single_type
        self.collection_type = collection_type

    def get(self, id):
        item = self.api_client.get(self.single_type, id)
        item.metadata['api_client'] = self.api_client
        return item

    def list(self, where=None):
        return self.api_client.list(self.collection_type, filter=where)
        
    def all(self):
        return self.api_client.all(self.collection_type)

    def new(self):
        pass
