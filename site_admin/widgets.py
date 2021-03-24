from django.forms import widgets
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(widgets.ClearableFileInput):
    clear_checkbox_label = _('Remove')
    input_text = _('')
    template_name = 'site_admin/custom_widget_templates/custom_clearable_file_input.html'


class CustomClearableFileInputImages(widgets.ClearableFileInput):
    clear_checkbox_label = _('Change')
    input_text = _('')
    template_name = 'site_admin/custom_widget_templates/custom_clearable_file_input_images.html'
