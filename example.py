from spire import ApiClient

# Credentials and server info
hostname = 'better-snow-2961.spirelan.com'
username = 'ApiUser'
password = 'Spire123!'
port = 10880

# Instantiate the Spire SDK with some credentials
spire = ApiClient(hostname, username, password, port=port)

# Get the list of Companies
# companies = spire.Companies.list()

# Extract a list of company names from the company list data
# company_names = sorted([company.name for company in companies])

# print the list of company names
# print(company_names)

# Get the very first company from the company list
# first_company = spire.Companies.list().first()

# Print the name of the company selected
# print("First Company: ", first_company.name)

# Get a reference to a specific company
company = spire.Company('inspire2021')

# Get the information for the selected company
# company_info = company.info()

# Print out the current company name and description
# print("Selected Company: ", company_info.name, ' - ', company_info.description)

# Get a list of Customers from the company
customers = company.Customers.list()

# print a list of the received customer names
print([customer.name for customer in customers])

# Get a single Customer by cust_no from the company using a filtered list, 
# use the one method because we expect one result
specific_customer = company.Customers.list(where=('{"customerNo":"FORHIS"}')).one()

# Print the customerNo to verify that we got the correct customer
print(specific_customer.customerNo)
#edit_customer = specific_customer.edit()
#edit_customer.save()

customer1 = company.Customers.get(2)
edit_customer1 = customer1.edit()
edit_customer1.name = "SDK CUSTOMER"
edit_customer1.hold = False
customer1.save()
customer1.delete()

# Get a list of all of the customers from the company
#customers = company.Customers.all()

# Print a list of the company's customer ids and confirm how many records we got
#print([customer.id for customer in customers], '\n', f"Received {len(customers)} records")

# Get a list of orders from the company
#orders = company.SalesOrders.all()

# Print a list of the orderNos for the orders received
#print([order.orderNo for order in orders])

# Get the first sales order from all sales orders
#order = company.SalesOrders.all().first()

# Print the orderNo
#print(order.customer.customerNo)