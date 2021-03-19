from django.urls import path
from .views import (
    admin_home, admin_edit_product,
    admin_edit_delivery
)

urlpatterns = [
    path('home/', admin_home, name='admin_home'),
    path('edit/<product_slug>/',
         admin_edit_product,
         name='admin_edit_product'),
    path('edit-delivery/',
         admin_edit_delivery,
         name='admin_edit_delivery'),
]
