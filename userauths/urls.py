from django.urls import path

from userauths import views

app_name="userauths"

urlpatterns=[
    path('sign-up/', views.registerUser, name="sign-up"),
    path('sign-in/', views.login_View, name="sign-in"),
    path('sign-out/', views.logout_View, name="sign-out"),
    path('forgotpassword', views.forgotpassword, name="emailpassword"),
]