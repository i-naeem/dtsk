from django.db.models import Model
from django.db.models import CASCADE
from django.db.models import SET_NULL
from django.db.models import CharField
from django.db.models import ImageField
from django.db.models import ForeignKey
from django.db.models import DecimalField
from django.db.models import DateTimeField
from django.db.models import BigIntegerField


class Order(Model):
    created_at = DateTimeField(
        verbose_name="Created at",
        auto_now_add=True,
        auto_created=True
    )

    def __str__(self) -> str:
        return self.pk


class Product(Model):
    name = CharField(
        max_length=255,
        verbose_name="Product Name",
        help_text="The name of the product"
    )

    price = DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Product Price",
        help_text="The price of the product"
    )

    quantity = BigIntegerField(
        verbose_name="Product Quantity",
        help_text="The quantity of the product"
    )

    order_id = ForeignKey(
        to=Order,
        related_name="order",
        verbose_name="Order ID",
        on_delete=SET_NULL
    )

    def __str__(self) -> str:
        return self.name


class Image(Model):
    product = ForeignKey(
        to=Product,
        on_delete=CASCADE,
        related_name="product_image",
        verbose_name="Product",
        help_text="The product in the images"
    )

    image = ImageField(
        null=True,
        blank=True,
        upload_to="images/",
        verbose_name="Product Image",
    )
