from django.urls import path, include
from . import  views

app_name="customer"


urlpatterns=[
    path('changepassword/', views.change_password_view, name="change_new_password")
]