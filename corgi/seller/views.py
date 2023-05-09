from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from homepage.views import homepage
from .models import *
from buyer.models import CartOrder, Cart, Slip
from .forms import NewSellerForm, ProductForm, EditProductForm, SellerProfile
from core.models import User

@login_required
def sbase(request): # Seller Homepage
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
def store_profile(request):
    userid = request.user.id
    username = User.objects.get(id=userid)
    seller = get_object_or_404(Seller, user_id=userid)
    context = {"seller":seller,
               "user": username}
    return render(request, "store_profile.html", context)

@login_required    
def edit_store(request):
    user = request.user.id
    try:
        seller = get_object_or_404(Seller, user_id=user)
        print(seller)
        form = SellerProfile(instance=seller)
        context = {'form': form }
        if request.method == "POST":
            form = SellerProfile(request.POST, request.FILES, instance=seller)
            if form.is_valid():
                print('valid')
                form.save()
        return render(request, "edit_store.html", context)
    except:
        context = {}
    return render(request, "edit_store.html", context)

@login_required    
def seller_product(request): # view seller product
    userID = request.user.id
    sellerID = None
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
    if request.method == "POST": # delete product form
        delete_product = request.POST.getlist('products[]')
        print(delete_product)
        for product_id in delete_product:
            product = get_object_or_404(SellerProduct, id=product_id)
            product.delete()
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

@login_required
def sproduct_detail(request, name):
    products = SellerProduct.objects.filter(name=name.replace('_', ' '))
    context = {'products': products}
    user = request.user.id
    print(f'{user}')
    return render(request, 'sproduct_detail.html', context)


@login_required
def edit_product(request, id):
    category = SellerCategory.objects.all()
    product = get_object_or_404(SellerProduct, pk=id, seller=request.user.seller)
    if request.method == "POST":
        print(product)
        form = EditProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
    else:
        form = EditProductForm(instance=product)
    context = {
        "products": product,
        "form": form,
        "categories": category,
    }
    return render(request, "edit_product.html", context)

@login_required
# def order_status(request, order_id):
#     order = get_object_or_404(CartOrder, order=order_id)
#     customer = order.customer
#     carts = Cart.objects.filter(customer=customer)
#     cart_items = []
#     for cart in carts:
#         cart_items.append({
#             'product': cart.product.name,
#             'quantity': cart.quantity,
#             'price': cart.price
#         })
#     total_cost = order.total_cost
#     slip = Slip.objects.filter(order=order).last()
    
#     return render(request, 'seller/order_status.html', {
#         'order_id': order_id,
#         'customer_name': f'{customer.first_name} {customer.last_name}',
#         'customer_phone': customer.phone,
#         'customer_email': customer.email,
#         'cart_items': cart_items,
#         'total_cost': total_cost,
#         'slip': slip
#     })

def order_status(request):
    cust = request.user
    buyer_firstname = cust.first_name
    buyer_lastname = cust.last_name
    buyer_phone = cust.phone

    slip = Slip.objects.first()  
    qrcode_image = slip.slip_image

    user = request.user.id
    carts = Cart.objects.filter(customer=user)
    cart_items = len(carts)
    cart_price = []
    for p in carts:
        cart_price.append(p.price) 
    total = sum(cart_price)
    order = CartOrder.objects.filter(customer_id=user, is_paid=False)
    orderID = order.last()

    # return render(request, 'seller/order_status.html', 
    context = {
        'order_id': orderID.order,
        'buyer_firstname': buyer_firstname,
        'buyer_lastname': buyer_lastname,
        'buyer_phone': buyer_phone,
        'qrcode_image': qrcode_image,
        'cart_items': cart_items,
        'total_price': total,
    }
    return render(request, 'order_status.html', context)
