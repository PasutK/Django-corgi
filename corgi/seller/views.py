from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from homepage.views import homepage
from .models import *

def Slogin(request):
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful. Enjoy Corgi!")
            return redirect(homepage)
        else:
            messages.success(request,"Wrong Username or Password, please try again")
            return redirect(Slogin)
    else:
        return render(request, 'Slogin.html', {})
    
def register_seller(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Register complete")
    return render(request, 'Sregister.html', {})

def logout_seller(request):
    return render(request, 'Slogout.html', {})

def sbase(request):
    return render(request, "Sbase.html", {})

# def seller_product_list(request):
#     # products = SellerProduct.objects.filter(seller=request.user.seller)
#     products = SellerProduct.objects
#     context = {'products': products}
#     return render(request, 'product_list.html', context)

def seller_product_list(request):
    seller = Seller.objects.filter(first_name=request.user).first()
    products = SellerProduct.objects.filter(seller=seller)
    context = {'products': products}
    return render(request, 'product_list.html', context)