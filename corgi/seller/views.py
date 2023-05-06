from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from homepage.views import homepage
from .models import *
from .forms import NewSellerForm
from core.models import User



def sbase(request):
    return render(request, "Sbase.html", {})

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
        print(request.POST)
    #if form.is_valid():
        # future clean up - createa fucntion to register the user
        registered_username = request.POST["username"]
        registered_password = request.POST["password1"]
        registered_email = request.POST["email"]
        registered_firstname = request.POST["first_name"]
        registered_lastname = request.POST["last_name"]

        user = User.objects.create_user(username=registered_username,
                                        password=registered_password,
                                        first_name=registered_firstname,
                                        last_name=registered_lastname,
                                        email=registered_email)
        user.save()

        seller_profile = SellerProfile.objects.create
            # form.save()
            # username = form.cleaned_data["username"]
            # password = form.cleaned_data["password1"]
            # user = authenticate(username=username, password=password)
            # login(request, user)


        #def create_Seller(self, user):
        #    seller = self.create(user)


        messages.success(request, "Your store has created!")
        return redirect('/seller/products') 
    else:  
        form = NewSellerForm()
    return render(request, 'Sregister.html', {'form': form })

def logout_seller(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return render(request, 'Slogout.html', {})


def seller_product(request):
    seller_products = SellerProduct.objects.all()

    context = {
        'seller_products': seller_products
    }

    return render(request, 'seller_product.html', context)
