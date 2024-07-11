from django.shortcuts import render, redirect
from django.urls import reverse
from wgql import forms
from wgql import models


def index(request):

    return render(request, 'index.html', {})


def create_product(request):
    context = {"product_form": forms.ProductForm()}

    if request.method == "POST":
        pf = forms.ProductForm(request.POST)
        images = request.FILES.getlist("image_url")

        if pf.is_valid():
            p = pf.save()
            for img in images:
                img = models.ProductImages(image_url=img, product=p)
                img.save()

            return redirect(reverse('index'))

    return render(request, "create_product.html", context)


def create_images(request):
    return render(request, 'create_images.html', {})


def create_order(request):
    context = {"form": forms.OrderForm()}

    if request.method == "POST":
        form = forms.OrderForm(request.POST)

        if form.is_valid():
            order = form.save()
            for product_id in dict(form.data).get('products'):
                product = models.Product.objects.get(id=product_id)
                product.order_id = order
                product.save()

            return redirect(reverse('index'))

    return render(request, 'create_order.html', context)
