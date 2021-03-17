from django import forms

from .models import Product, ProductFeature, ProductImage
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = 'name', 'description', 'price'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductFeatureForm(forms.ModelForm):

    class Meta:
        model = ProductFeature
        fields = 'feature',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 ,b-0'
        for field in self.fields:
            self.fields[field].label = False


class ProductImageForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        fields = 'image',

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False


ProductFeatureFormset = forms.inlineformset_factory(
        Product,
        ProductFeature,
        form=ProductFeatureForm,
        fields=('feature',),
        extra=1,
        max_num=6
    )

ProductImageFormset = forms.inlineformset_factory(
        Product,
        ProductImage,
        form=ProductImageForm,
        fields=('image',),
        extra=4,
        max_num=4,
    )
