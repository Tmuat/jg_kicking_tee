from decimal import Decimal

from django.shortcuts import get_object_or_404

from products.models import Product
from checkout.models import DeliveryOptions


def bag_contents(request):

    bag_items = []
    delivery_option = []

    total = 0
    delivery_cost = 0
    grand_total = 0
    product_count = 0

    bag = request.session.get('bag', {})
    delivery_array = request.session.get('delivery', {})

    for product_sku, quantity in bag.items():
        product = get_object_or_404(Product, sku=product_sku)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product_sku': product_sku,
            'quantity': quantity,
            'product': product
            })

    for delivery_sku, price in delivery_array.items():
        delivery = get_object_or_404(
            DeliveryOptions, delivery_sku=delivery_sku)
        delivery_cost = Decimal(price)
        delivery_option.append({
            'delivery': delivery
        })

    if delivery_cost > 0:
        delivery_set = True
    else:
        delivery_set = False

    grand_total = total + delivery_cost

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'delivery_option': delivery_option,
        'delivery_set': delivery_set,
        'total': total,
        'grand_total': grand_total
    }

    return context
