from django.conf import settings
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from django.urls.conf import partial
from . import views

app_name = 'games'
urlpatterns = [

    path('', views.Games.as_view(), name='games'),
    path('<str:game_id>/', views.game, name='game'),

]
