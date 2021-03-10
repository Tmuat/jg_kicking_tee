from django.shortcuts import render, get_object_or_404

from .models import Product, ProductImage


def product_detail(request, product_slug):
    """ A view to show individual product details """

    product = get_object_or_404(Product, slug=product_slug)
    product_images = ProductImage.objects.filter(product=product)

    context = {
        'product': product,
        'product_images': product_images
    }

    return render(request, 'products/product_detail.html', context)
