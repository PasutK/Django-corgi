from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from seller.models import SellerCategory, SellerProduct

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

def category_detail(request, name):
    products = SellerProduct.objects.filter(name=name)
    context = {'products': products}
    return render(request, 'product_detail.html', context)






