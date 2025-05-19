from django.contrib import admin
from django.urls import path
from .views import temperature_request, redirect_request

urlpatterns = [
    path('temperature-request', temperature_request, name='temperature-request'),
    path('', redirect_request)
]
