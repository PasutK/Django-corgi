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

@login_required    
def seller_product(request):
    sellers = Seller.objects.all()
    sellerID = request.GET.get("Seller")
    print(sellerID)
    print(sellers)
    if sellerID:
        product = SellerProduct.objects.filter(id__in=sellerID)
        seller = Seller.objects.get(id=sellerID)
    else:
        product = SellerProduct.objects.all()
        seller = None
    context = {
        "product": product,
        "sellers": sellers,
        "seller": seller,
        "sellerID": sellerID
    }

    return render(request, "seller_product.html", context)
