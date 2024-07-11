from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import ProductForm
from .models import Product
from .models import Image


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products": products})


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {"product": product})


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
