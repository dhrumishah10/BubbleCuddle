from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request,'products/home.html')
def ourstory(request):
    return render(request,'products/ourstory.html')
def contactus(request):
    return render(request,'products/contactus.html')
