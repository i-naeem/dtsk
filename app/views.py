from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products": products})


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {"product": product})
