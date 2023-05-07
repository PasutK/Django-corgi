from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from homepage.views import homepage
from .models import *
from .forms import NewSellerForm, ProductForm
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
    # userID = request.user.id
    sellerID = Seller.objects.get(user__id=request.user.id)
    products = SellerProduct.objects.filter(seller__id=sellerID.id)
    # products = SellerProduct.objects.all()
    print(f'products: {products}')
    print(f'sellerID: {sellerID}')
    if sellerID:
        product = SellerProduct.objects.filter(seller__id=sellerID.id)
        # seller = Seller.objects.get(id=sellerID)
    else:
        product = SellerProduct.objects.all()
    #     seller = None
    context = {
        "products": product,
        # "sellers": sellers,
        # "seller": seller,
        "sellerID": sellerID
    }

    return render(request, "seller_product.html", context)

@login_required
def add_product(request, **kwargs):
    store_name = kwargs.get('store_name')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'add_product.html', context=context)



