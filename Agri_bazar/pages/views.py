from django.shortcuts import render
from store.models import Product
from category.models import Category

# Create your views here.

def index(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'product_dict': product_list,
        'category_dict': category_list
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')
