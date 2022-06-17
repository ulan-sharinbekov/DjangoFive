from django.contrib import admin
from django.urls import path, include
from .views import get_list_categories, get_list_articles, get_article, create_article

urlpatterns = [
    path('categories/', get_list_categories, name="get_list_categories"),
    path('', get_list_articles, name="get_list_articles"),
    path('<int:pk>', get_article),
    path('create/', create_article, name="add_article")

]
