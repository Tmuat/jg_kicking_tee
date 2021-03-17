from django.urls import path

from .views import product_detail, edit_product


urlpatterns = [
    path('product/<product_slug>', product_detail, name='product_detail'),
    path('edit/<product_slug>/', edit_product, name='edit_product'),
]
