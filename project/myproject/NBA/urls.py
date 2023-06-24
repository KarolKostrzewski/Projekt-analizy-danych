from django.urls import path
from . import views

urlpatterns = [
    path('', views.nba, name='nba'),
    path('post/', views.nba_postseason, name='nba_postseason'),
]