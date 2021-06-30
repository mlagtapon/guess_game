from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('process_guess', views.process),
    path('clear', views.clear),
]