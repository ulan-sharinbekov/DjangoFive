from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Categories"



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    creation_date = models.DateField(default=timezone.now)
    image = models.TextField(default=None)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    view = models.IntegerField(default=0)
