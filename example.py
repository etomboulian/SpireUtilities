from spire import ApiClient

hostname = 'better-snow-2961.spirelan.com'
username = 'ApiUser'
password = 'Spire123!'
port = 10880

# Instantiate the Spire SDK with some credentials
spire = ApiClient(hostname, username, password, port=port)

# Get the list of Companies
companies = spire.Companies.list()

# Extract a list of company names from the company list data
company_names = sorted([company.name for company in companies])

# print the list of company names
print(company_names)

# Get a reference to a specific company
company = spire.Company('inspire2021')

# Print out the current company name and description
print(company.info().name)
print("Selected Company: ", company.info().description)

# Get a list of Customers from the company
customers = company.Customers.list()
print([customer.name for customer in customers])

# Get a single Customer by cust_no from the company
specific_customer = company.Customers.list(where=('{"customerNo":"FORHIS"}'))
print(specific_customer[0].customerNo)

specific_customer = company.Customers.get("2")
print(specific_customer.customerNo)

customers = company.Customers.all()
print([customer.name for customer in customers])

# Get a list of orders from the company
#orders = company.SalesOrders.list()
#print(orders)


