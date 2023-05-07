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
    userID = request.user.id
    sellerID = None
    print(userID)
    if userID:
        try:
            sellerID = Seller.objects.get(user__id=request.user.id)
            product = SellerProduct.objects.filter(seller__id=sellerID.id)
        except:
            product = SellerProduct.objects.all()
    else:
        product = SellerProduct.objects.all()
    context = {
        "products": product,
        "sellerID": sellerID
    }

    return render(request, "seller_product.html", context)

@login_required
def edit_or_add_product(request, product_id=None):
    sellers = request.user.seller