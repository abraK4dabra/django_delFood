from . import views
from django.urls import path
from products.views import products, basket_add, basket_delete, baskets

app_name = "products"

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('categories/<int:id>/', views.category_detail, name='category_detail'),
    path('page/<int:page>', products, name='page'),
    path('basket', baskets, name='baskets'),
    path('basket-add/<int:product_id>', basket_add, name='basket_add'),
    path('basket-delete/<int:basket_id>', basket_delete, name='basket_delete'),
]
