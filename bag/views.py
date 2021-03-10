from django.shortcuts import render, redirect, get_object_or_404

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
    else:
        bag[product.sku] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
