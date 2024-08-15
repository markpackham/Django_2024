from django.shortcuts import render
from .form import ContactForm

# Create your views here.

# The homepage view function
def home_view(request):
    return render(request, 'form_app/home.html')