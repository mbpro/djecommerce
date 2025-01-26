from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from userauths import forms as userauths_form
from vendor import models as vendor_models
from userauths import  models as userauths_models


# Create your views here.
def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return  redirect('/')

    form= userauths_form.UserRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save()

        full_name=form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password1')
        user_type=form.cleaned_data.get('user_type')


        user=authenticate(email=email, password=password)
        login(request, user)

        messages.success(request,'Account was created Successfully')
        profile=userauths_models.Profile.objects.create(full_name=full_name, mobile=mobile,user=user)

        if user_type=='Vendor':
            vendor_models.Vendor.objects.create(user=user,store_name=full_name)
            profile.user_Type='Vendor'
        else:
            profile.user_Type='Customer'
        profile.save()

        next_url=request.GET.get("next","/")
        return redirect(next_url)


    context={
        "form":form
    }

    return render(request, "userauths/sign-up.html", context)


def login_View(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return  redirect('/')

    if request.method=="POST":
        form=userauths_form.LoginForm(request.POST or None)

        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')

            try:
                user_instance=userauths_models.User.objects.get(email=email, is_active=True)
                user_authenticate=authenticate(request, email=email, password=password)

                if user_instance is not None:
                    login(request, user_authenticate)
                    messages.success(request,"You are logged in!")

                    next_url = request.GET.get("next", "/")
                    return redirect(next_url)
                else:
                    messages.error(request, "Username or Password does not exist")
            except:
                messages.error(request, "User does not exist")
    else:
        form=userauths_form.LoginForm()

    context={
        "form":form
    }

    #return  redirect(request, "userauths:sign-in", context)
    return render(request, "userauths/login-in.html", context)

def logout_View(request):
    if 'cart_id' in request.session:
        cart_id=request.session['cart_id']
    else:
        cart_id=None
    logout(request)
    request.session['cart_id']=cart_id
    messages.success(request, "You are logged out!")

    return  redirect("userauths:sign-in")

def forgotpassword(request):
    return render(request, "userauths/forgotpass.html")