from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from category.models import Category
from customers.models import Customer

# Create your views here.

def index(request):
    product_list = None
    category_list = Category.objects.all()
    category_filter = request.GET.get('category')
    product_list = Product.get_all_products_by_categoryid(category_filter)

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
    if request.method == 'GET':
        return render(request, 'pages/signup.html')
    else:
        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        mobile_num = request.POST.get('Mobile_Number')
        email = request.POST.get('Email')
        address = request.POST.get('Address')
        password = request.POST.get('Password')

        data = Customer(first_name=first_name,
                        last_name=last_name,
                        mobile_number=mobile_num,
                        email=email,
                        address=address,
                        password=password)
        data.save()

        return HttpResponse("success")

def single_product(request):
    return render(request, 'pages/single_product.html')
