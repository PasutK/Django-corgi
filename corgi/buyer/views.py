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
    # for cart_item in cart:
        # print(cart_item.product)
    # context = {'cart_items': cart_items, 'total_price': total_price}
    context = {'carts': carts,
               'total': total,}
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    if request.method == 'POST':
        cart = request.session.pop('cart', None)

        if cart:
            for item in cart.values():
                product = SellerProduct.objects.get(name=item['name'])
                product.quantity -= item['quantity']
                product.save()

            # transaction = Transaction.objects.create(user=request.user, cart=cart)
            # return redirect('thank_you')

    return render(request, 'checkout.html')

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


# @login_required
# def chat(request):
#     seller = Seller.objects.all() # assuming the user id is the same as the seller id
#     context = {'store_name': seller.store_name}
#     return render(request, 'chat.html', context=context)


@login_required
def chat(request, store_name):
    stores = Seller.objects.filter(store_name=store_name)
    print(f"store:{stores}")
    context = {'stores': stores}
    return render(request, 'chat.html', context=context)
