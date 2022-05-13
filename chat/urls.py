from django.conf import settings
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from django.urls.conf import partial
from . import views

app_name = 'chat'
urlpatterns = [

    path('', views.DialogsView.as_view(), name='chats'),
    path('create/', views.createDialog, name='create'),
    path('search/', views.search, name='search'),
    path('<str:chat_id>/', views.MessagesView.as_view(), name='chat'),
    path('api/messages/', views.GetMassagesInfoView.as_view(), name='message_api')
]
