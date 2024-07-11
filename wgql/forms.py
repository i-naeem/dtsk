from django import forms
from wgql.models import Product, ProductImages


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_quantity", "product_price"]
