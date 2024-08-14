from django.shortcuts import render

# Create your views here.
def index(request):
    # With linux & unix devices use "/"
    # return render(request, 'tours/index.html')
    return render(request, 'tours\index.html')