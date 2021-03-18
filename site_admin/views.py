from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404


from checkout.models import Order
from products.models import Product
from .forms import (
    ProductForm,
    ProductFeatureFormset,
    ProductImageFormset
)


def admin_home(request):
    """
    A view to return the admin home page.
    """

    orders = Order.objects.all().order_by('-date')[:8]

    context = {
        'orders': orders,
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
