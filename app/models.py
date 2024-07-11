from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Image(models.Model):
    image = models.ImageField(upload_to="products/")
