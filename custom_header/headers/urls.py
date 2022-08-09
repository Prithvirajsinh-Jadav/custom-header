from django.urls import path

from . import views

urlpatterns = [
    path('headers/', views.index, name='index'),
]