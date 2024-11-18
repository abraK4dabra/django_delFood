from django.contrib import admin

from products.models import ProductCategory, Product, Basket


# Register your models here.
# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Basket)
