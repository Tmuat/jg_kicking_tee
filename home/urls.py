from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('my-story/', views.my_story, name='my_story')
]