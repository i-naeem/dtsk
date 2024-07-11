from django.contrib import admin

from .models import Product
from .models import Order
from .models import Image

admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Product)
