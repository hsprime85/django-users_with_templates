from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.add_user),
]
