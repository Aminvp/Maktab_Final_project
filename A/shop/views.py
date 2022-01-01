from django.shortcuts import render
from .models import Product, Category


def home(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/home.html')