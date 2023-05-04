from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from seller.models import SellerCategory, SellerProduct, Seller

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
    context = {'products': products}
    return render(request, 'category_detail.html', context)

def product_detail(request, category, name):
    products = SellerProduct.objects.filter(category=category, name=name.replace('_', ' '))
    context = {'products': products}
    return render(request, 'product_detail.html', context)

def store_detail(request, store_name):
    store = Seller.objects.filter(store_name=store_name.replace('_', ' '))
    context = {'store': store}
    return render(request, 'store_detail.html', context)
