from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import FormRegistration, Editprofile
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from homepage.views import homepage
from buyer.views import Bhomepage
from buyer.models import *

def userlogin(request):
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful. Enjoy Corgi!")
            return redirect(homepage)
        else:
            messages.success(request,"Wrong Username or Password, please try again")
            return redirect(userlogin)
    else:
        return render(request, 'login.html', {})

def userlogout(request):
    logout(request)
    return render(request, "logout.html", {})

def userregister(request):
    form = FormRegistration(request.POST)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        new_user.save()
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect(Bhomepage)
    return render(request, "register.html", {'form':form})


@login_required
def userprofile(request):
    return render(request, "profile.html", {})

@login_required
def viewprofile(request):
    userID = request.user.id
    user = get_object_or_404(User,id=userID)
    context = {'user':user}
    return render(request, "userprofile.html", context)

@login_required
def editUser_profile(request):
    user = request.user
    if request.method == 'POST':
        cust = Editprofile(request.POST, instance=user)
        if cust.is_valid():
            cust.save()
            messages.success(request, "updated success!")
            previous_url = request.POST.get('previous_url')
            return redirect(previous_url)
    else:
        cust = Editprofile(instance=user)
    context = {'cust': cust,}
    return render(request, 'edituserprofile.html', context)

@login_required
def order_status(request):
    userID = request.user.id
    order = CartOrder.objects.filter(customer = userID)
    print(order)
    context={
        'order': order ,
            }
    return render(request, "order_status.html", context)