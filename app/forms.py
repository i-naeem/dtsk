from django import forms
from .models import Order
from .models import Product
from .models import Image


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "quantity"]


class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text="Select the products for this order"
    )

    class Meta:
        model = Order
        fields = ["products"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "product"]
