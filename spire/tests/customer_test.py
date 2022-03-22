from datetime import datetime
from spire import ApiClient

print("Running customer test script")

# Instantiate the Spire SDK with some credentials
spire = ApiClient('better-snow-2961.spirelan.com', 'ApiUser', 'Spire123!', port=10880)

# Get a connection to inspire2021 company
inspire = spire.Company('inspire2021')

# Print a list of the names of all the customers from the first page of the customer list
print([customer.name for customer in inspire.Customers.list()])

# Get a list of all customers
customers = inspire.Customers.all()

# Print a list of all customer ids that exist in the system
print([customer.id for customer in customers])

# Print the total number of customers in the all collection
print(len(customers))

# Get a the customer with customerNo FORHIS
forhis = inspire.Customers.get(2)

# Change the customer name to a unique value
forhis.name = f"TEST CUSTOMER {datetime.now()}"

# Save the customer back into the database
forhis.save()

print()