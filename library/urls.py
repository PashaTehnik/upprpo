from django.urls import path, include
from . import views

urlpatterns = [
    path('games', views.index),
    path('', views.index),
]
