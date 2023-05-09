from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from seller.models import SellerCategory, SellerProduct, Seller
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Q
from .forms import *
from core.models import User
import random
from django.views import View
from decimal import Decimal
# Create your views here.

def Bhomepage(request):
    allproducts = SellerProduct.objects.all()
    random_products = random.sample(list(allproducts.values_list('id',flat=True)), 9)
    feature_product = SellerProduct.objects.filter(id__in=random_products)
    context = {'products':feature_product}
    return render(request, "store base.html",context)

def category_list(request):
    categories = SellerCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category):
    products = SellerProduct.objects.filter(category=category)
#    print(f"product:{products}")
    for product in products:
        print(f"product: {product}")
    
    context = {'products': products}
    return render(request, 'category_detail.html', context)

def product_detail(request, category, name):
    products = SellerProduct.objects.filter(category=category, name=name.replace('_', ' '))
    sellerproduct = products.first()
    productprice = sellerproduct.price
    product = get_object_or_404(SellerProduct, pk=sellerproduct.id)
    context = {'products': products}
    user = request.user.id
    customer = get_object_or_404(User, pk=user)
    print(product,customer)
    form = AddtoCart(request.POST)
    if request.method == "POST":
        quantity = request.POST.get("amount")
        price = productprice * Decimal(quantity)
        add_to_cart = Cart(product=product, price=price, amount=quantity, customer=customer)
        add_to_cart.save()
        context = {'products': products, 'form':form}
    return render(request, 'product_detail.html', context)

def store_detail(request, store_name):
    stores = Seller.objects.filter(store_name=store_name.replace('_', ' '))
    print(f"store:{stores}")
    context = {'stores': stores}
    return render(request, 'store_detail.html', context)

@login_required
def cart(request):
    user = request.user.id
    carts = Cart.objects.filter(customer=user)
    cart_price = []
    for p in carts:
        cart_price.append(p.price)
    total = sum(cart_price)
    context = {'carts': carts,
               'total': total,}
    return render(request, 'cart.html', context)

@login_required
def checkout(request):
    # Get the user's name and phone number from their login data
    buyer_name = request.user.username
    buyer_phone = request.user.phone
    store_name = Seller.store_name
    store_address = Seller.store_address
    qrcode_image = Seller.qrcode_image
    # Retrieve the cart data
    user = request.user.id
    carts = Cart.objects.filter(customer=user)
    cart_price = []
    for p in carts:
        cart_price.append(p.price)
    total = sum(cart_price)

    # Define the context variables
    context = {
        'buyer_name': buyer_name,
        'buyer_phone_number': buyer_phone,
        'store_name': store_name,
        'store_address': store_address,
        'qrcode_image': qrcode_image,
        'carts': carts,
        'total': total,
    }

    return render(request, 'checkout.html', context)



@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        products = SellerProduct.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) 
        )
    else:
        products = SellerProduct.objects.all()
    return render(request, 'search.html', {'products': products})

def payment_status(request):
    # Retrieve the order information from the database
    user = request.user.id
    carts = Cart.objects.filter(customer=user)
    cart_items = len(carts)
    cart_price = []
    for p in carts:
        cart_price.append(p.price) 
    total = sum(cart_price)

    # Define the context variables
    context = {
        'order_id': '123456',  # Replace with actual order ID
        'order_date': 'May 9, 2023',  # Replace with actual order date
        'cart_items': cart_items,
        'total_price': total,
        'payment_status': 'Pending',  # Replace with actual payment status
    }

    return render(request, 'payment_status.html', context)

@login_required
def edit_profile(request):
    userid = request.user.id
    userprofile = User.objects.filter(pk=userid).first()
    context = {'user': userprofile}
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_user')
    else:
        form = EditProfileForm(instance=userprofile)
    context = {
        'form': form,
    }
    return render(request, "edit_profile.html", context)


@login_required
def chat(request, store_name):
    stores = Seller.objects.filter(store_name=store_name)
    print(f"store:{stores}")
    context = {'stores': stores}
    return render(request, 'chat.html', context=context)
