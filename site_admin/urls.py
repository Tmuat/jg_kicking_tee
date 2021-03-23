from django.urls import path
from .views import (
    admin_home, admin_edit_product,
    admin_edit_delivery,
    OrdersListView,
    dispatch_orders,
    complete_orders
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
         OrdersListView.as_view(),
         name='admin_orders'),
    path('dispatch/',
         dispatch_orders,
         name='dispatch_orders'),
    path('complete/',
         complete_orders,
         name='complete_orders'),
]
