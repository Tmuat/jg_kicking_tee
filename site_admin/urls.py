from django.urls import path
from .views import (
    admin_home, admin_edit_product,
    admin_edit_delivery,
    all_orders,
    dispatch_orders,
    complete_orders,
    order_detail
)

urlpatterns = [
    path('home/', admin_home, name='admin_home'),
    path('edit/<product_slug>/',
         admin_edit_product,
         name='admin_edit_product'),
    path('edit-delivery/',
         admin_edit_delivery,
         name='admin_edit_delivery'),
    path('orders/',
         all_orders,
         name='admin_orders'),
    path('order/<order_number>/',
         order_detail,
         name='order_detail'),
    path('dispatch/',
         dispatch_orders,
         name='dispatch_orders'),
    path('complete/',
         complete_orders,
         name='complete_orders'),
]
