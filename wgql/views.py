from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def create_product(request):
    return render(request, 'create_product.html', {})


def create_images(request):
    return render(request, 'create_images.html', {})


def create_order(request):
    return render(request, 'create_order.html', {})
