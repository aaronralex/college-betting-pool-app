
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='bettingpool-history'),
    path('scores/', views.scores, name='bettingpool-scores'),
    path('about/', views.about, name='bettingpool-about'),
    path('elements/', views.elements, name='bettingpool-elements'),
    path('generic/', views.generic, name='bettingpool-generic'),
]