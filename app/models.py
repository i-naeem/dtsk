from django.db import models


class Order(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Order Created Date",
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.pk}"


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Product Name",
        help_text="Enter the name of the product"
    )

    quantity = models.IntegerField(
        default=1,
        verbose_name="Product Quantity",
        help_text="Enter the quantity of the product"
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Product Price",
        help_text="Enter the price of the product"
    )

    order = models.ForeignKey(
        to=Order,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Order",
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Product Image",
        help_text="Select the product image"
    )

    def __str__(self):
        return self.image.name
