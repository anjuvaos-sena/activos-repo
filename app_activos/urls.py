from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: redirect('activos')),
    path('activos/', views.activos_view, name='activos'),
]