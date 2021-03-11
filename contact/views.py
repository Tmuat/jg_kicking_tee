from honeypot.decorators import check_honeypot

from django.shortcuts import render, redirect
from django.core.mail import (
    BadHeaderError,
    EmailMessage
)
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages

from .forms import (
    ContactForm
)

from .models import (
    EmailInfo
)


@check_honeypot
def contact(request):
    """
    A view to return the contact page. A honeypot is included
    to stop bots submitting the form.
    """
    form = ContactForm()
    email = EmailInfo.objects.first()
    website_email = str(
        '"' + email.email_show_name + '" <' + email.email + '>'
    )

    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['from_name']
            form_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            msg_contact = render_to_string('contact/emails/contact.txt',
                                           {'name': name,
                                            'email': form_email,
                                            'message': message})

            msg_contact_confirm = render_to_string('contact/emails/contact-confirm.txt',
                                                   {'name': name,
                                                    'email': email,
                                                    'message': message})
            try:
                email = EmailMessage(
                    "Website Contact",
                    msg_contact,
                    website_email,
                    [website_email],
                    reply_to=[form_email],
                )
                email.send(fail_silently=False)
                email_confirm = EmailMessage(
                    "Contact Confirmation",
                    msg_contact_confirm,
                    website_email,
                    [form_email],
                )
                email_confirm.send(fail_silently=False)
                messages.success(request, 'Thank you for submitting '
                                 'the contact form')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')

    context = {
        "form": form,
    }

    template = 'contact/contact.html'

    return render(request, template, context)
