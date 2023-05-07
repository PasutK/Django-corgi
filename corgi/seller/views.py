from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from homepage.views import homepage
from .models import *
from .forms import NewSellerForm
from core.models import User


@login_required
def sbase(request):
    return render(request, "Sbase.html", {})

@login_required    
def register_seller(request):
    if request.method == "POST":
        form = NewSellerForm(request.POST, request.FILES)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
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
