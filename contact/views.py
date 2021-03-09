from honeypot.decorators import check_honeypot

from django.shortcuts import render

from .forms import (
    ContactForm
)


@check_honeypot
def contact(request):
    """
    A view to return the contact page. A honeypot is included
    to stop bots submitting the form.
    """
    form = ContactForm()

    context = {
        "form": form,
    }

    template = 'contact.html'

    return render(request, template, context)
