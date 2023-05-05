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
    if request.method == "POST":
        form = NewSellerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your store has created!")
            return redirect('/seller/products') 
    else:  
        form = NewSellerForm()
    return render(request, 'Sregister.html', {'form': form })

# def vendor_register(request):
#     if request.method == 'POST':
#         form = VendorForm(request.POST, request.FILES)
#         if form.is_valid():
#             vendor = form.save(commit=False)
#             vendor.user = request.user
#             vendor.save()
#             messages.success(request, 'Your vendor account has been created!')
#             return redirect('vendor:my_products')
#     else:
#         form = VendorForm()
#     return render(request, 'vendor_registration.html', {'form': form})


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
