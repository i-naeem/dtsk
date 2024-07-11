from django.forms import ModelMultipleChoiceField
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm
from .models import Product
from .models import Order


class OrderForm(ModelForm):
    products = ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=CheckboxSelectMultiple,
        help_text="Select the product to create order"
    )

    class Meta:
        model = Order
        fields = ["products"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "quantity", "price"]
