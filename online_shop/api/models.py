from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    MEN = 'MEN'
    WOMEN = 'WOMEN'
    KIDS = 'KIDS'
    CATALOG_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (KIDS, 'Kids'),
    ]
    type = models.CharField(max_length=200)
    catalog = models.CharField(max_length=200, choices=CATALOG_CHOICES)


class Product(models.Model):
    title = models.CharField(max_length=200)
    articule = models.CharField(max_length=30, unique=True)
    price = models.FloatField()
    currency = models.CharField(max_length=20)
    count = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ratingg = models.FloatField()


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    grade = models.FloatField()



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)
