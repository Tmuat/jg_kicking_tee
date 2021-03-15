from django.conf import settings

from django.contrib import messages

from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('home'))

    order_form = OrderForm()

    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key
    }

    return render(request, template, context)

