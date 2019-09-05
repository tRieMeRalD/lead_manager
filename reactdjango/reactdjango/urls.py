from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Front end loads before leads IMPORTANT
    path("", include("frontend.urls")),
    path('', include("leads.urls"))
]
