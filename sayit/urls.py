from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/<int:player_id>', views.play, name='play'),
    path('save/', views.save_player, name='save_player'),
]