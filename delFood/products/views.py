from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    context = {
        "title": "delFood",
    }
    return render(request, "products/index.html", context)


def baskets(request):
    context = {
        "title": "корзина",
    }
    return render(request, "products/index.html", context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def products(request):
    context = {
        "title": "каталог",
        "products": Product.objects.all()
    }
    return render(request, "products/products.html", context)


def food_carousel(request):
    context = {
        "title": "каталог",
        "products": Product.objects.all()
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')
