from django.shortcuts import render


def view_bag(request):
    """
    A view to return the shopping bag.
    """

    context = {
    }

    template = 'bag/bag.html'

    return render(request, template, context)
