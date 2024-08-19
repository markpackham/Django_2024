from django.shortcuts import render
from .forms import ProductForm
from .models import Product

def home_view(request):
    return render(request, 'invApp/home.html')
