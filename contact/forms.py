from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


class ContactForm(forms.Form):
    from_name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'rows': 5})
