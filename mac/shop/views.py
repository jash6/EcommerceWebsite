from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    n= len(products)
    nslides =n//4 +ceil((n/4)-(n//4))
    params={'no_of_slides': nslides, 'range': range(1,nslides),'product': products} 
    return render(request ,"shop/index.html",params)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return render(request, "shop/contact.html")

def tracker(request):
    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")

def searchlocation(request):
    return render(request, "shop/contact.html")

def productview(request):
    return render(request, "shop/productview.html")

def checkout(request):
    return render(request, "shop/checkout.html")