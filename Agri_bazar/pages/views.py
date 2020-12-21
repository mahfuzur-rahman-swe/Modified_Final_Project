from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product
from category.models import Category
from customers.models import Customer
from django.contrib.auth.hashers import make_password, check_password



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

#login page
def login_page(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    else:
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        customer = Customer.login_email_exits(email)
        error_message = None
        if customer:
            password_check = check_password(password, customer.password)
            if password_check:
                request.session['customer_id'] = customer.id
                return redirect('index')

            else:
                error_message = 'Email or Password Incorrect..!!'
                return render(request, 'pages/login.html')
        else:
            error_message = 'Email or Password Incorrect..!!'
            return render(request, 'pages/login.html', {'error': error_message})

#signup page
def signup(request): #signup page
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

        data = Customer(first_name=first_name,
                        last_name=last_name,
                        mobile_number=mobile_num,
                        email=email,
                        address=address,
                        password=password)

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
            error_message = 'Password required !!'
        elif data.signup_email_exits():
            error_message = 'Email already registered'
        elif len(password) < 5:
            error_message = 'Password must be five character long'

        if not error_message:
            data.password = make_password(data.password)
            data.save()
            return redirect('index')

        else:
            values = {
                'first_name': first_name,
                'last_name': last_name,
                'mobile_number': mobile_num,
                'email': email,
                'address': address,
            }
            dictionary = {
                'error': error_message,
                'value': values
            }
            return render(request, 'pages/signup.html', dictionary)

def single_product(request):
    return render(request, 'pages/single_product.html')

#about page
def about(request):
    return render(request, 'pages/about.html')
