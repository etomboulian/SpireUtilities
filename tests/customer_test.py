from datetime import datetime
from ..spire.api_client import ApiClient

hostname = 'better-snow-2961.spirelan.com'
username = 'ApiUser'
password = 'Spire123!'
port = 10880

# Instantiate the Spire SDK with some credentials
spire = ApiClient(hostname, username, password, port=port)

# Get a connection to inspire2021 company
inspire = spire.Company('inspire2021')

# Print a list of the names of all the customers from the first page of the customer list
print([customer.name for customer in inspire.Customers.list()])

# Print a list of all customer ids that exist in the system
print([customer.id for customer in inspire.Customers.all()])

# Get a the customer with customerNo FORHIS
forhis = inspire.Customers.get(2)

# Change the customer name to a unique value
forhis.name = f"TEST CUSTOMER {datetime.now}"

# Save the customer back into the database
forhis.save()
