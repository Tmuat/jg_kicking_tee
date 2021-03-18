from django.shortcuts import render


from checkout.models import Order


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
