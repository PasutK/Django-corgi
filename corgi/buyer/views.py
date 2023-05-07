from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from seller.models import SellerCategory, SellerProduct, Seller
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Q
import random
from django.views import View
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
    context = {'products': products}
    user = request.user.id
    print(f'{user}')
    return render(request, 'product_detail.html', context)

class Index(View):
    def get(self, request):
        print(f"1.{request.get_full_path()}")
        return HttpResponseRedirect(f'store'+f"{request.get_full_path().split('buyers/')[1]}")
    
    def post(self, request):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart
        print("cart", request.session["cart"])
        print(f"{request.get_full_path()}")
        return redirect("homepage")

def store_detail(request, store_name):
    stores = Seller.objects.filter(store_name=store_name.replace('_', ' '))
    print(f"store:{stores}")
    context = {'stores': stores}
    return render(request, 'store_detail.html', context)

@login_required
def cart(request):
    cart_items = []
    total_price = 0  # Define total_price outside of the if block

    if 'cart' in request.session:
        cart = request.session.get('cart', {})

        for item in cart.values():
            cart_items.append(item)
            total_price += item['total_price']

    context = {'cart_items': cart_items, 'total_price': total_price}
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
