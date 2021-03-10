from products.models import (
    Product,
)


def global_product(request):
    return {
        'product': Product.objects.first(),
    }
