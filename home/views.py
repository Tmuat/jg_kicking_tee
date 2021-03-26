from random import shuffle, sample

from django.shortcuts import render

from .models import LandingImage, Testimonial


def index(request):
    """
    A view to return the index page. Including admin uploaded images for
    the gallery.
    """

    images_qs = list(LandingImage.objects.filter(active=True))

    if len(images_qs) < 9:
        sample_len = len(images_qs)
    else:
        sample_len = 10

    images_qs_sample = sample(images_qs, k=sample_len)

    testimonial_qs = list(Testimonial.objects.filter(active=True))
    shuffle(testimonial_qs)

    context = {
        'images': images_qs_sample,
        'testimonials': testimonial_qs,
    }

    template = 'home/index.html'

    return render(request, template, context)


def my_story(request):
    """
    A view to return the my story page.
    """

    context = {

    }

    template = 'home/my_story.html'

    return render(request, template, context)
