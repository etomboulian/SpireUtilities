
from .status import Status

# Company Single and List Types
from .companies import CompanyLinks, CompanyList

# Customer Single and List Types
from .customers.customer import CustomerDetail as Customer
from .customers.customer_list import CustomerList 

# Sales Order Single and List Types
from .sales.orders.order import Order as SalesOrder
from .sales.orders.order_list import SalesOrderList

# Invoice Single and List Types
from .sales.invoices.invoice import Invoice
from .sales.invoices.invoice_list import InvoiceList