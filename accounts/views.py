from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers' : customers,'total_customers' : total_customers,
               'total_orders' : total_orders, 'delivered' : delivered, 'pending' :pending }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products' : products})

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer.html', {'customers' : customers})