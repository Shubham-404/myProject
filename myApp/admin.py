from django.contrib import admin
from myApp.models import SellerInfo, cart, customer, product, order
# Register your models here.
admin.site.register(SellerInfo)
admin.site.register(cart)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)