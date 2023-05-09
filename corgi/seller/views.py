from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from homepage.views import homepage
from .models import *
from .forms import NewSellerForm, ProductForm, EditProductForm
from core.models import User

@login_required
def sbase(request):
    user = request.user.id
    print(user)
    try:
        seller = Seller.objects.filter(user_id=user).first().user_id
        print(seller)
    except:
        seller=None
    if user == seller:
        return render(request, "Sbase.html", {})
    else:
        return redirect("/seller/register")



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
def add_product(request):
    categories = SellerCategory.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            product = form.save(commit=False)
            product.seller = request.user.seller
            product.save()
            return redirect("seller/products")
    else:
        form = ProductForm()
    context = {
        "form": form,
        "categories":categories
        }
    return render(request, "add_product.html", context)
    # for c in categories:
    #     print(c.name)
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     category = request.POST.get("category")
    #     price = request.POST.get("price")
    #     status = request.POST.get("status")
    #     description = request.POST.get("description")
    #     image = request.POST.get("image")
    #     print(name)
    #     print(category)
    #     print(price)
    #     print(status)
    #     print(description)
    #     print(image)

def sproduct_detail(request, name):
    products = SellerProduct.objects.filter(name=name.replace('_', ' '))
    context = {'products': products}
    user = request.user.id
    print(f'{user}')
    return render(request, 'sproduct_detail.html', context)

def delete_products(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products[]')
        SellerProduct.objects.filter(id__in=product_ids).delete()
        return redirect('seller_product')
    else:
        return render(request, 'seller_product.html')


def edit_product(request, id):
    category = SellerCategory.objects.all()
    product = get_object_or_404(SellerProduct, pk=id, seller=request.user.seller)
    if request.method == "POST":
        print(product)
        form = EditProductForm(request.POST,request.FILES,instance=product)
    else:
        form = EditProductForm(instance=product)
    context = {
        "products": product,
        "form": form,
        "categories": category,
    }
    return render(request, "edit_product.html", context)


from buyer.models import Cart


def payment_overview(request):
    # Retrieve the order information from the database
    orders = Cart.objects.all()

    # Define the context variables
    context = {
        'orders': orders,
    }

    return render(request, 'payment_overview.html', context)
