from .models import ProductCategory


def categories_context(request):
    categories = ProductCategory.objects.all()
    return {'categories': categories}
