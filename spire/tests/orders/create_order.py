from spire import ApiClient

spire = ApiClient('better-snow-2961.spirelan.com', 'ApiUser','Spire123!', port=10880)
inspire = spire.Company('inspire2021')
data = {'customer': {'customerNo': 'LYNDIS'}}
new_order = inspire.SalesOrders.new(data)
print(new_order)
#new_order.save()