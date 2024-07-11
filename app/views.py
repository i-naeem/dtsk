from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.urls import reverse
from .forms import ProductForm
from .forms import OrderForm
from .models import Product
from .models import Image
from .models import Order


def index(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'index.html', {"products": products, "orders": orders})


def product(request, product_id):
    product = get_object_or_404(
        Product.objects.select_related(), pk=product_id)

    return render(request, 'product.html', {"product": product})


def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = Product.objects.filter(order=order)

    return render(request, 'order.html', {"products": products})


def create_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save()
            for image in request.FILES.getlist('product-images'):
                product_image = Image(product=product, image=image)
                product_image.save()

            return redirect(reverse('app:product', kwargs={"product_id": product.id}))

    context = {"form": ProductForm()}
    return render(request, 'create_product.html', context)


def create_order(request):

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            for product_id in dict(form.data).get('products'):
                product = Product.objects.get(pk=product_id)
                product.order = order
                product.save()

            return redirect(reverse('app:order', kwargs={"order_id": order.id}))

    context = {"form": OrderForm()}
    return render(request, 'create_order.html', context)
