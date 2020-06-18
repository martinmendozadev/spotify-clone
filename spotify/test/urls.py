"""Test URL's."""

# Django
from django.urls import path

# Views
from spotify.test import views


urlpatterns = [
    path('', views.hello, name='hello'),
]
