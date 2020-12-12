from django.shortcuts import render
from store.models import Product
from category.models import Category

# Create your views here.

def index(request):
    product_list = None
    category_list = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        product_list = Product.get_all_products_by_categoryid(category_id)
    else:
        product_list = Product.objects.all()
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

def single_product(request):
    return render(request, 'pages/single_product.html')
