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

# Read view
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})

# Update view
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST":