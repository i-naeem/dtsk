
from django.db import models


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=True)
    # TODO: When switching to POSTGRESQL change this to ArrayField
    products = models.CharField(max_length=120, default="")

    def __str__(self) -> str:
        return f"{self.order_id}:{self.order_date}"


class Product(models.Model):
    product_name = models.CharField(
        max_length=255, help_text="Enter the name of the product")
    product_quantity = models.PositiveIntegerField(
        help_text="Enter the quantity of the product")
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Enter the price of the product")


class ProductImages(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.ImageField(
        upload_to='product_images/', help_text="Select the product images")

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
