from spire import ApiClient

spire = ApiClient('better-snow-2961.spirelan.com', 'ApiUser','Spire123!', port=10880)
inspire = spire.Company('inspire2021')
new_order = inspire.SalesOrders.new()
new_order.customer.customerNo = 'LYNDIS'
new_order.save()