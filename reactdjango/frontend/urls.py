from django.urls import path
from . import views

urlspatterns = [
    path("", views.index) # The views.py index method we just created
]