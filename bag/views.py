from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view to return the shopping bag.
    """

    context = {
    }

    template = 'bag/bag.html'

    return render(request, template, context)


def add_to_bag(request, product_id):
    """
    Add a quantity of specified product to the shopping bag.
    """
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product.sku in list(bag.keys()):
        bag[product.sku] += quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[product.sku]}'))
    else:
        bag[product.sku] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, product_id):
    """
    Adjust the quantity of specified product to the shopping bag.
    """
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product.sku] = quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[product.sku]}'))
    else:
        bag.pop(product.sku)
        messages.success(request,
                         (f'Removed {product.name} '
                          f'from your bag'))

    request.session['bag'] = bag

    return redirect(reverse('bag'))


def remove_from_bag(request, product_id):
    """
    Remove the item from the shopping bag.
    """

    try:
        product = get_object_or_404(Product, id=product_id)
        bag = request.session.get('bag', {})

        bag.pop(product.sku)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
