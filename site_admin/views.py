from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mass_mail, BadHeaderError
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string

from checkout.models import Order
from products.models import Product, ProductStock
from contact.models import EmailInfo
from .forms import (
    ProductForm,
    ProductFeatureFormset,
    ProductImageFormset,
    DeliveryFormset,
    TestimonialFormset,
    ProductStockForm
)


@staff_member_required
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


@staff_member_required
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


@staff_member_required
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


@staff_member_required
def admin_edit_testimonials(request):
    """
    A view to Edit home screen testimonials.
    """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        formset = TestimonialFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Successfully updated testimonials!')
            return redirect(reverse('admin_edit_testimonials'))
        else:
            messages.error(request,
                           ('Failed to update testimonials. '
                            'Please ensure the form is valid.'))
    else:
        formset = TestimonialFormset()

    template = 'site_admin/admin_testimonial.html'
    context = {
        'formset': formset,
    }

    return render(request, template, context)


@staff_member_required
def all_orders(request):
    """
    A view to show all orders, including filtering and search queries
    """

    order_page = True
    order_list = Order.objects.all().order_by('-date')
    query = None
    page = request.GET.get('page', 1)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']

            queries = Q(order_number__icontains=query) \
                | Q(full_name__icontains=query)
            order_list = order_list.filter(queries)

    paginator = Paginator(order_list, 25)
    num_pages = paginator.num_pages

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    template_name = 'site_admin/admin_orders.html'

    context = {
        'order_page': order_page,
        'orders': orders,
        'num_pages': num_pages,
        'query': query,
    }

    return render(request, template_name, context)


@staff_member_required
def order_detail(request, order_number):
    """
    A view to show individual order details
    """

    order = get_object_or_404(Order, order_number=order_number)

    template = 'site_admin/admin_order_detail.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@staff_member_required
def stock_levels(request, product_slug):
    """
    A view to show individual product stock levels
    """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    initial_product = get_object_or_404(Product, slug=product_slug)

    product_stock = get_object_or_404(ProductStock, product=initial_product)

    form = ProductStockForm(instance=product_stock)

    if request.method == 'POST':
        form = ProductStockForm(request.POST, instance=product_stock)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated stock!')
            return redirect(reverse('admin_home'))
        else:
            messages.error(request,
                           ('Failed to update stock. '
                            'Please ensure the form is valid.'))

    template = 'site_admin/admin_product_stock.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def dispatch_orders(request):
    """
    Change the status of orders to dispatched.
    """
    email = EmailInfo.objects.first()
    website_email = str(
        '"' + email.email_show_name + '" <' + email.email + '>'
    )

    if request.method == 'POST':
        selected = request.POST.get('id-selected')
        ids = selected.split(",")
        email_messages = list()
        for count, order_id in enumerate(ids):
            order = Order.objects.get(id=order_id)
            if order.status == "dispatched" or order.status == "complete":
                pass
            else:
                message_name = str('dispatch_message' + str(count))
                subject = ("JimmyG Kicking Tee Dispatch Notice:" +
                           f"{order.order_number}")
                message = render_to_string('site_admin/emails/dispatch_email.txt',
                                           {'order': order})
                message_name = (
                    subject,
                    message,
                    website_email,
                    [order.email])
                email_messages.append(message_name)
        try:
            send_mass_mail(email_messages, fail_silently=False)
            messages.success(request, 'Dispatch Emails Sent!')
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        Order.objects.filter(id__in=ids).update(status="dispatched")

    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)


@staff_member_required
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
