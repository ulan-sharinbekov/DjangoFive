from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from article.models import Article

# Create your models here.

class Comment(models.Model):
    description = models.TextField()
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    creation_date = models.DateField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
