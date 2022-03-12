from pySpireClient import ApiClient

hostname = 'better-snow-2961.spirelan.com'
username = 'ApiUser'
password = 'Spire123!'

# Instantiate the Spire SDK with some credentials
spire = ApiClient(hostname, username, password)

# Get the list of Companies
result = spire.Companies.list()

# Get a reference to a specific company
company = spire.Company('inspire2021')

# Get a list of orders from the company
orders = company.SalesOrders.list()

# Get a list of Customers from the company
customers = company.Customers.list()

# Get a single Customer by cust_no from the company
specific_customer = company.Customers.get('ACTTEC')