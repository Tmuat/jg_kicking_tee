from django.forms import widgets
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(widgets.ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Images')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'


widgets.CheckboxInput.template_name = 'products/custom_widget_templates/delete.html'


