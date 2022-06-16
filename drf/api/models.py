from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name, self.country}'

class Vehicle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    year = models.IntegerField(default=1990)
    color = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title, self.year, self.color, self.type}'
