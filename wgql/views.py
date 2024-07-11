from django.shortcuts import render

from .models import Product


def index(request):
    return render(request, 'index.html', {})


def product(request):
    context = {
        "products": Product.objects.prefetch_related('product_image').all()
    }
    return render(request, 'product/index.html', context)


def create_product(request):
    context = {}
    return render(request, "product/create.html", context)


"""

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

"""
