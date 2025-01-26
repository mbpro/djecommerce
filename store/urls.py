from django.urls import path
from. import views

app_name="store"

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    path('detail/', views.details, name="detail"),
    path('checkout/', views.checkout, name="checkout"),
    path('shop/', views.shop, name="shop"),
    path('detail/<slug>/', views.detail_view, name="details_view"),




]