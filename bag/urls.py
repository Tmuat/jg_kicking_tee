from django.urls import path

from . import views


urlpatterns = [
    path('shopping-bag/', views.view_bag, name='bag')
]
