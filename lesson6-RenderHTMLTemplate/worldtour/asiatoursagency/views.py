from django.shortcuts import render
from .models import Tour

# Create your views here.
def index(request):
    tours = Tour.objects.all()
    context = {'tours':tours}
    # With linux & unix devices use "/"
    # return render(request, 'tours/index.html')
    return render(request, 'tours\index.html',context)