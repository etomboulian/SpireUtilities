from argparse import Namespace
import requests
import json
from requests.models import HTTPBasicAuth

from .utils.spire_json_encoder import SpireJsonEncoder
from .models import Model

class ApiClient:
    headers = {'Content-Type': 'application/json'}
    proxies = {'https':'http://127.0.0.1:8080'}

    root_endpoints = {
        'status': 'status',
        'companies': 'companies/'
    }

    company_endpoints = {
        'status': 'status/',
        'sales_orders': 'sales/orders/',
        'sales_order_items': 'sales/items',
        'customers': 'customers/'
    }

    def __init__(self, hostname, username, password, port=10880):
        self.root_url = f'https://{hostname}:{port}/api/v2/'

        self.auth = HTTPBasicAuth(username, password)
        if not self.logged_in():
            raise Exception("Unable to authenticate with Spire")
        

    def check_response(self, response):
        if response.status_code == 400:
            raise Exception('400 - Bad Request')
        elif response.status_code == 401:
            raise Exception('401 - Authentication Required: You need to be authenticated to access this resource')
        elif response.status_code == 403:
            raise Exception('403 - Forbidden: The logged in user does not have permission to access this resource')
        elif response.status_code == 404:
            raise Exception('404 - Resouce not found')
        elif response.status_code == 420:
            raise Exception('420 - Collection qill return too many results: Use a filter to limit the results')
        elif response.status_code == 422:
            raise Exception('422 - Unprocessible Entity (a required field might be missing or contain invalid data)')
        elif response.status_code == 421:
            raise Exception('421 - Record Locked, Close the record you are currently working on')
        elif response.status_code >= 400:
            raise Exception(f'{response.status_code} - {response.text}')

        try:
            response = response.json()
        except Exception:
            raise Exception('Unable to decode response ' + Exception.message)

        return response

    def logged_in(self):
        endpoint = self.root_endpoints['status']
        url = self.root_url + endpoint
        
        response = requests.get(url, auth=self.auth, verify=False)

        # throws an exception if there is a problem with the response
        try:
            response = self.check_response(response)

            # Check to see that we got a version in the json response to determine if we are logged in or not
            if 'version' in response:
                return True
            else:
                return False
        except Exception as e:
            print('Exception', e)
            pass

    def create(self, data: Model) -> object:
        if data.endpoint is None:
            raise Exception('Unable to Create resource as the type of resource to be created is unknown. model.endpoint is None')

        endpoint = data.endpoint
        response = requests.post(self.company_url + endpoint, headers=self.headers, proxies=None, auth=self.auth, data=json.dumps(o, cls=SpireJsonEncoder), verify=False)

        self.check_response(response)

        if (response.status_code == 201):
            # then we have successs
            # now do a second request to the value in the Location header and return that object
            secondRequest = response.headers.get("Location")
            createdItem = requests.get(secondRequest, auth=self.auth, verify=False)
            item_str = createdItem.content.decode()
            createdObject = json.loads(item_str, object_hook=lambda d: Namespace(**d))
            return createdObject

    def update(self, id : int, data: Model) -> object:
        if data.endpoint is None:
            raise Exception('Unable to Create resource as the type of resource to be created is unknown. model.endpoint is None')
            
        endpoint = self.company_endpoints[type]
        response = requests.put(self.company_url + endpoint, headers=self.headers, proxies=None, auth=self.auth, data=json.dumps(data, cls=SpireJsonEncoder), verify=False)

        self.check_response(response)

        if response.status_code == 200:
            updatedObject_str = response.content.decode()
            updatedObject = json.loads(response.content.decode(), object_hook=lambda d: Namespace(**d))
            return updatedObject
        

    def get(self, id : int) -> object:
        response = requests.get(self.base_url, headers=self.headers, proxies=None, auth=self.auth, verify=False)

    def list(self, search_string: str, max_records : int) -> list():
        pass

    def delete(self, id : int) -> bool:
        pass