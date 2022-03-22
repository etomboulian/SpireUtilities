from spire import ApiClient

spire = ApiClient('better-snow-2961.spirelan.com', 'ApiUser','Spire123!', port=10880)

inspire = spire.Company('inspire2021')

for order in inspire.SalesOrders.all():
    if order.shippingAddress.shipId != "":
        if order.customerPO != order.shippingAddress.shipId:
            order.customerPO = order.shippingAddress.shipId
            order.save()