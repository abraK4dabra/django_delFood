from django.shortcuts import render
# from products.models import ProductCategory, Product


# Create your views here.


def index(request):
    context = {
        "title": "delFood",
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        "title": "каталог",
    }
    return render(request, "products/products.html", context)


# def login(request):
#     return render(request, 'users/login.html')
#
#
# def register(request):
#     return render(request, 'users/register.html')
