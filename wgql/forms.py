from django import forms
from wgql.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_quantity", "product_price"]


class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text="Select the products for this order"
    )

    class Meta:
        model = Order
        fields = ["products"]
