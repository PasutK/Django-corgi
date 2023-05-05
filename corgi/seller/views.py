from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from homepage.views import homepage
from .models import *
from .forms import NewSellerForm

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
    form = NewSellerForm()
    if request.method == "POST":
        form = NewSellerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Register complete")
            return redirect(homepage)
    return render(request, 'Sregister.html', {'form': form })

def logout_seller(request):
    return render(request, 'Slogout.html', {})

def sbase(request):
    return render(request, "Sbase.html", {})

def seller_product(request):
    seller_products = SellerProduct.objects.all()

    context = {
        'seller_products': seller_products
    }

    return render(request, 'seller_product.html', context)
