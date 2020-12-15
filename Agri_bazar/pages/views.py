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

        #validation
        error_message = None

        if not first_name:
            error_message = 'First Name Required !!'
        elif len(first_name) < 4:
            error_message = 'First Name must be four character long'
        elif not last_name:
            error_message = 'Last Name Required !!'
        elif len(first_name) < 4:
            error_message = 'Last Name must be four character long'
        elif not mobile_num:
            error_message = 'Mobile Number Required !!'
        elif len(mobile_num) < 11:
            error_message = 'Mobile Number must be eleven character long'
        elif not password:
            error_message = 'Password Required !!'
        elif len(password) < 5:
            error_message = 'Passwords must be at least 5 characters long'
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_number': mobile_num,
            'email': email,
            'address': address,
        }

        if not error_message:
            data = Customer(first_name=first_name,
                            last_name=last_name,
                            mobile_number=mobile_num,
                            email=email,
                            address=address,
                            password=password)
            data.save()
            return render(request, 'pages/signup.html')
        else:
            dictionary = {
                'error': error_message,
                'value': values
            }
            return render(request, 'pages/signup.html', dictionary)

def single_product(request):
    return render(request, 'pages/single_product.html')
