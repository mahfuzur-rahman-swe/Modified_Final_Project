from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    weight = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='photos/product/%y/%m/%d')

    def image_validation(self):

        if not self.image:
            raise ValidationError("No image!")
        else:
            w, h = get_image_dimensions(self.image)
            if w != 140:
                raise ValidationError("The image is %i pixel wide. It's supposed to be 140px" % w)
            if h != 140:
                raise ValidationError("The image is %i pixel high. It's supposed to be 140px" % h)

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    def __str__(self):
        return self.name
