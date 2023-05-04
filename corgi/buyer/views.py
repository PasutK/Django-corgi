from django.shortcuts import render
from .models import Category

# Create your views here.
def Blogin(request):
    pass

def Blogout(request):
    pass

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})