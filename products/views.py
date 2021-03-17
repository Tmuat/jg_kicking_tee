from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404


from .models import Product, ProductImage, ProductFeature
from .forms import (
    ProductForm,
    ProductFeatureFormset,
    ProductImageFormset
)


def product_detail(request, product_slug):
    """ A view to show individual product details """

    product = get_object_or_404(Product, slug=product_slug)
    product_images = ProductImage.objects.filter(product=product)
    product_features = ProductFeature.objects.filter(product=product)

    context = {
        'product': product,
        'product_images': product_images,
        'product_features': product_features
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def edit_product(request, product_slug):
    """
    Edit a product in the store
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

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'formset': formset,
        'image_formset': image_formset,
        'product': product,
    }

    return render(request, template, context)
