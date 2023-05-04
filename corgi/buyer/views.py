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

def product_category(request, pk):
    products = SellerProduct.objects.filter(category__pk=pk)
    context = {'products': products}
    return render(request, 'product_list.html', context)

def product_detail(request, pd):
    products = SellerProduct.objects.filter(product__pd=pd)
    context = {'products': products}
    return render(request, 'product_detail.html', context)





