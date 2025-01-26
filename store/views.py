from django.shortcuts import render
from store import models as store_models
from django.db.models import Sum, Count


# Create your views here.

def index(request):
    products = store_models.Product.objects.filter(status='Published')
    category=store_models.Category.objects.all()
    #related_product = store_models.Product.objects.filter(category=products.category, status="Published")
    featured_products= store_models.Product.objects.filter(status='Published', featured=True)
    count_categories= 0



    context={
        'products':products,
        'category':category,
        'featured_products':featured_products,
        'count_categories':count_categories,

    }
    print(products)
    return render(request, "store/index.html",context)

def detail_view(request, slug):
    product=store_models.Product.objects.get(status="Published", slug=slug)
    related_product=store_models.Product.objects.filter(category=product.category, status="Published").exclude(
        id=product.id)

    context={
        "product": product,
        "related_product": related_product,
    }

    return render(request, "store/product_detail.html", context)



def contact(request):
    return  render(request, "store/contact.html")

def cart(request):
    return  render(request, "store/cart.html")

def details(request):
    return render(request, "store/product_detail.html")

def checkout(request):
    return  render(request, "store/checkout.html")

def shop(request):
    product_list = store_models.Product.objects.filter(status='Published', featured=True)

    context = {
        "product_list": product_list,
    }

    return  render(request, "store/shop.html", context)



