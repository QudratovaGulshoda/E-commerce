from django.shortcuts import render
from .models import Product
def home_view(request):
    products = Product.objects.all().order_by('?')
    d = {
        'products':products
    }
    return render(request, 'index.html', context=d)

def blog_view(request):
    return render(request, 'index-2.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def contact_view(request):
    return render(request, 'contact.html')

def cart_view(request):
    return render(request, 'cart.html')