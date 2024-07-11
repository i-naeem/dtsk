from django.contrib import admin

from wgql.models import Order
from wgql.models import Product
from wgql.models import ProductImages

# Register your models here.
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductImages)
