from django.contrib import admin
from django.urls import path, include
from .views import signup

urlpatterns = [
    path('signup', signup, name="add_user")
]
