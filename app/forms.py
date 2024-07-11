from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "quantity"]


# class OrderForm(forms.ModelForm):
#     products = forms.ModelMultipleChoiceField(
#         queryset=Product.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         help_text="Select the products for this order"
#     )

#     class Meta:
#         model = Order
#         fields = ["products"]
