from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from seller.models import SellerCategory, SellerProduct, Seller
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Q

# Create your views here.
def Blogin(request):
    return render(request, "Blogin.html",{})

def Bregister(request):
    return render(request, "Bregister.html",{})

def Blogout(request):
    pass

def Bhomepage(request):
    return render(request, "store.html",{})

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
    return render(request, 'product_detail.html', context)

def store_detail(request, store_name):
    stores = Seller.objects.filter(store_name=store_name.replace('_', ' '))
    print(f"store:{stores}")
    context = {'stores': stores}
    return render(request, 'store_detail.html', context)

# def add_to_cart(request, product_id):
#     product = SellerProduct.objects.get(id=product_id)
#     quantity = int(request.POST.get('quantity'))
#     total_price = product.price * quantity

#     if 'cart' not in request.session:
#         request.session['cart'] = {}

#     cart = request.session['cart']

#     if product_id not in cart:
#         cart[product_id] = {'name': product.name, 'image': product.image.url, 'quantity': quantity, 'price': product.price, 'total_price': total_price}
#     else:
#         cart[product_id]['quantity'] += quantity
#         cart[product_id]['total_price'] = cart[product_id]['quantity'] * cart[product_id]['price']

#     request.session.modified = True
#     return redirect('cart')

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

@require_POST
def add_to_cart(request):
    product_id = request.POST['product_id']
    amount = int(request.POST['amount'])
    product = Product.objects.get(pk=product_id)
    cart = cart(request)
    cart.add(product, amount)
    return redirect('cart')

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


def search(request):
    query = request.GET.get('q')
    if query:
        products = SellerProduct.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) 
        )
    else:
        products = SellerProduct.objects.all()
    return render(request, 'search.html', {'products': products})





