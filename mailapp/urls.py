from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('r1/',send_emails),
]
