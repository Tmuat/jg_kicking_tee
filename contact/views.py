from honeypot.decorators import check_honeypot

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string

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
    print(website_email)

    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['from_name']
            email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            subject = "Website Inquiry"

            msg_contact = render_to_string('emails/contact.txt',
                                           {'name': name,
                                            'subject': subject,
                                            'email': email,
                                            'message': message})

            msg_contact_confirm = render_to_string('emails/contact-confirm.txt',
                                                   {'name': name,
                                                    'subject': subject,
                                                    'email': email,
                                                    'message': message})
            try:
                email = EmailMessage(
                    subject,
                    msg_contact,
                    '"JG Kicking Tee" <Thomas_Muat@hotmail.com>',
                    ['"JG Kicking Tee" <Thomas_Muat@hotmail.com>'],
                    reply_to=[email],
                )
                email.send(fail_silently=False)
                send_mail(
                    "Contact Confirmation",
                    msg_contact_confirm,
                    '"JG Kicking Tee" <Thomas_Muat@hotmail.com>',
                    [email],
                    fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')

    context = {
        "form": form,
    }

    template = 'contact.html'

    return render(request, template, context)
