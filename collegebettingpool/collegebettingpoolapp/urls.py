
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='bettingpool-history'),
    path('scores/', views.scores, name='bettingpool-scores'),
    path('about/', views.about, name='bettingpool-about'),
]