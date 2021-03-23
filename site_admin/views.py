from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView

from checkout.models import Order
from products.models import Product
from .forms import (
    ProductForm,
    ProductFeatureFormset,
    ProductImageFormset,
    DeliveryFormset
)


def admin_home(request):
    """
    A view to return the admin home page.
    """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    order_count = Order.objects.count()

    completed_order_count = Order.objects. \
        filter(status='complete').count()

    orders = Order.objects.all().order_by('-date')[:8]

    context = {
        'orders': orders,
        'order_count': order_count,
        'completed_order_count': completed_order_count
    }

    template = 'site_admin/admin_home.html'

    return render(request, template, context)


def admin_edit_product(request, product_slug):
    """
    A view to Edit a product in the store.
    """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=product_slug)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        formset = ProductFeatureFormset(
            request.POST,
            request.FILES,
            instance=product
        )
        image_formset = ProductImageFormset(
            request.POST,
            request.FILES,
            instance=product
        )
        if form.is_valid() and formset.is_valid() and image_formset.is_valid():
            form.save()
            formset.save()
            image_formset.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        formset = ProductFeatureFormset(instance=product)
        image_formset = ProductImageFormset(instance=product)

    template = 'site_admin/admin_product_management.html'
    context = {
        'form': form,
        'formset': formset,
        'image_formset': image_formset,
        'product': product,
    }

    return render(request, template, context)


def admin_edit_delivery(request):
    """
    A view to Edit delivery options.
    """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        formset = DeliveryFormset(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Successfully updated delivery!')
            return redirect(reverse('admin_edit_delivery'))
        else:
            messages.error(request,
                           ('Failed to update delivery. '
                            'Please ensure the form is valid.'))
    else:
        formset = DeliveryFormset()

    template = 'site_admin/admin_delivery.html'
    context = {
        'formset': formset,
    }

    return render(request, template, context)


class OrdersListView(ListView):

    template_name = 'site_admin/admin_orders.html'
    queryset = Order.objects.all()
    context_object_name = 'orders'
    paginate_by = 20
    ordering = ['-date']
    allow_empty_first_page = True


def dispatch_orders(request):
    """
    Change the status of orders to dispatched.
    """

    if request.method == 'POST':
        selected = request.POST.get('id-selected')
        ids = selected.split(",")
        Order.objects.filter(id__in=ids).update(status="dispatched")

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)


def complete_orders(request):
    """
    Change the status of orders to complete.
    """

    if request.method == 'POST':
        selected = request.POST.get('id-selected')
        ids = selected.split(",")
        Order.objects.filter(id__in=ids).update(status="complete")

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)
