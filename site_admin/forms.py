from django import forms

from products.models import (
    Product,
    ProductFeature,
    ProductImage,
    ProductStock
)
from checkout.models import DeliveryOptions
from home.models import (
    Testimonial,
    InstructionalVideo,
)
from .widgets import (
    CustomClearableFileInput,
    CustomClearableFileInputImages
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = 'name', 'description', 'price'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductStockForm(forms.ModelForm):

    class Meta:
        model = ProductStock
        fields = 'stock_quantity',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class VideoForm(forms.ModelForm):

    class Meta:
        model = InstructionalVideo
        fields = 'video',

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'border-black rounded-0'


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
        fields = 'image', 'rank'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 ,b-0'


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
        fields=('image', 'rank'),
        extra=4,
        max_num=4,
    )


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = DeliveryOptions
        fields = 'option', 'description', 'price', 'active'

    option = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, }))

    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs[
                'class'] = 'border-0 rounded-0 w-100 h-100 no-active'


DeliveryFormset = forms.modelformset_factory(
        DeliveryOptions,
        form=DeliveryForm,
    )


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = 'name', 'testimonial', 'image', 'active'

    testimonial = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={'rows': 9, }
        )
    )

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInputImages)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs[
                'class'] = 'border-0 rounded-0 w-100 h-100 no-active'


TestimonialFormset = forms.modelformset_factory(
        Testimonial,
        form=TestimonialForm,
    )
