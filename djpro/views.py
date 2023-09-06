from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return render(request,"contact.html")

def homepage(request):
    data = {
        'title' : "Homepage"
    }
    return render(request,"index.html",data)

def checkout(request):
    return render(request,"checkout.html")

def shop(request):
    return render(request,"shop.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

def detail(request):
    return render(request,"detail.html")

def cart(request):
    return render(request,"cart.html")

def index(request):
    return render(request,"index.html")

def view_details(request):
    return render(request,"view_details.html")