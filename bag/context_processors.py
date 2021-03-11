from django.shortcuts import get_object_or_404

from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_sku, quantity in bag.items():
        product = get_object_or_404(Product, sku=product_sku)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product_sku': product_sku,
            'quantity': quantity,
            'product': product
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count
    }

    return context
