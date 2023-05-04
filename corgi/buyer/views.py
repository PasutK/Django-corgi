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
    product = SellerProduct.get_object_or_404(Category, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)



