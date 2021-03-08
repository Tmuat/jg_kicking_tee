from random import shuffle


from django.shortcuts import render


from .models import LandingImage, Testimonial


def index(request):
    """
    A view to return the index page. Including admin uploaded images for
    the gallery.
    """

    images_qs = list(LandingImage.objects.filter(active=True))
    shuffle(images_qs)

    testimonial_qs = list(Testimonial.objects.filter(active=True))
    shuffle(testimonial_qs)

    context = {
        'images': images_qs,
        'testimonials': testimonial_qs
    }

    template = 'home/index.html'

    return render(request, template, context)
