from django.contrib import admin
from .models import Product

# Register your models here.
class Admin_Product(admin.ModelAdmin):
    list_display = ['name', 'price', 'weight', 'category']

admin.site.register(Product)
