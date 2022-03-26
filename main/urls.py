from django.urls import path, include
from . import views

urlpatterns = [
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_, name='logout'),
    #path('<str:id>/', views.login),
]
