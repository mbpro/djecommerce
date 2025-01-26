from django.shortcuts import render, redirect
from django.contrib import  messages
from django.contrib.auth.hashers import check_password

# Create your views here.








def change_password_view(request):
    if request.method =="POST":
        old_password=request.POST.get("oldpassword")
        new_password=request.POST.get("newpassword")
        confirm_password=request.POST.get("confirmpassword")


        if new_password != confirm_password:
            messages.error(request, "Password enetered not matching!")
            return redirect("customer:change_new_password")
        if check_password(old_password, request.user.password):
            request.user.set_password(new_password)
            request.save()
            messages.success(request, "Password was successfully changed!")
            return redirect("userauths:sign-in")
        else:
            messages.error(request, "Password is incorrect")
            return redirect("customer:change_new_password")
    return render(request, "customer/changepassword.html")