from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('product/single/', views.single_product, name = 'single_product'),
    path('about/', views.about, name = 'about'),
    path('login/', views.login_page, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout')
]
