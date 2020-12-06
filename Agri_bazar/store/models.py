from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    weight = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='photos/product/%y/%m/%d')

    def __str__(self):
        return self.name
