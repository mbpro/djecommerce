from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'posts/index.html')

def contact(request):
    return  render(request, 'posts/contact.html')

def cart(request):
    return render(request, 'posts/cart.html')

def checkout(request):
    return render(request, 'posts/checkout.html')

def detail(request):
    return render(request, 'posts/detail.html')

def shop(request):
    return  render(request, 'posts/shop.html')

