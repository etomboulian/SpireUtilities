from spire import ApiClient

hostname = 'better-snow-2961.spirelan.com'
username = 'ApiUser'
password = 'Spire123!'
port = 10880

print("Running company test script")

# Instantiate the Spire SDK with some credentials
spire = ApiClient(hostname, username, password, port=port)

# Print a list of all of the companies on the Spire server
print([company.name for company in spire.Companies.list()])

# Get a connection to inspire2021 company
inspire = spire.Company('inspire2021')

# Get company information about inspire2021
company_info = inspire.info()

# Print out customer info
print(f'Company Name: {company_info.name}, Description: {company_info.description}, needs_upgrad {company_info.needs_upgrade}')

print()