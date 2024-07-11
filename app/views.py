from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    return render(request, 'index.html', {})


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {"product": product})
