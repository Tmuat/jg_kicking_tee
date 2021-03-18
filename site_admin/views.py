from django.shortcuts import render


def admin_home(request):
    """
    A view to return the admin home page.
    """

    context = {
    }

    template = 'site_admin/admin_home.html'

    return render(request, template, context)
