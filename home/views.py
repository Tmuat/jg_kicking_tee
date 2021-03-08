from random import shuffle


from django.shortcuts import render


from .models import Image


def index(request):
    """
    A view to return the index page. Including admin uploaded images for
    the gallery.
    """

    images_qs = list(Image.objects.filter(active=True))
    shuffle(images_qs)

    context = {
        'images': images_qs,
    }

    template = 'home/index.html'

    return render(request, template, context)
