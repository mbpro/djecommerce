from django.urls import path
from. import views

app_name="posts"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    path('detail/', views.detail, name="detail"),
    path('checkout/', views.checkout, name="checkout"),
    path('shop/', views.shop, name="shop"),



]
