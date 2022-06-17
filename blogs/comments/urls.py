from django.contrib import admin
from django.urls import path, include
from .views import get_comments_of_article, create_comment

urlpatterns = [
    path('<int:pk>/', get_comments_of_article, name="get_comments_of_article"),
    path('<int:pk>/create/', create_comment, name="add_comment"),

]
