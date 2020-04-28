from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    print (request.method)
    return render(request, 'index.html', {'products': products})


def new(request):
    return render(request, 'index.html')
