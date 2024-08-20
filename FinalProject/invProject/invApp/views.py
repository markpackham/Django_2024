from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def home_view(request):
    return render(request, 'invApp/home.html')

def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        # Redirect if it is not a POST request
    return render(request, 'invApp/product_form.html', {'form':form})