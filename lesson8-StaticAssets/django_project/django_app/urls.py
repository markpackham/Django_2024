from django.urls import path
from .views import index

urlpatterns = [
    # NEVER forget to add the "," at the end or it will not work
    path('', index, name="index"),
]