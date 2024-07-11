from django.forms import ModelMultipleChoiceField
from django.forms import CheckboxSelectMultiple
from django.forms import ClearableFileInput
from django.forms import ModelForm
from .models import Product
from .models import Image
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


class Image(ModelForm):
    class Meta:
        model = Image
        fields = ["image"]
        widget = {
            'image': ClearableFileInput(attrs={'multiple': True, 'required': False})
        }
