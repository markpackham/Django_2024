from django.urls import path
from .form import ContactForm

def home_view(request):
    return render(request, 'form_app/')