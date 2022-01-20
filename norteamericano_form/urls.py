"""
LABX URLS
"""
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from . import api

urlpatterns = [
    path('validate_rut/<str:rut>', api.validate_rut , name='validate_rut'),
]

