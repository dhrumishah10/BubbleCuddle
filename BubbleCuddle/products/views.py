from django.shortcuts import render
from .models import product
# Create your views here.

from django.shortcuts import render

def home(request):
    prod = product.objects.all()
    return render(request,'products/home.html', {"prod":prod})
def ourstory(request):
    return render(request,'products/ourstory.html')
def contactus(request):
    return render(request,'products/contactus.html')