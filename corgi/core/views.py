from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import FormRegistration, Editprofile
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from homepage.views import homepage
from buyer.views import Bhomepage

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

# class UserRegisterView(CreateView):
#     form_class = FormRegistration
#     template_name = "register.html"
#     success_url = reverse_lazy("core:profile")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         form.save()
#         return response


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

#         registered_username = request.POST["username"]
#         registered_password = request.POST["password1"]
#         registered_email = request.POST["email"]
#         registered_firstname = request.POST["first_name"]
#         registered_lastname = request.POST["last_name"]

#         user = User.objects.create_user(username=registered_username,
#                                         password=registered_password,
#                                         first_name=registered_firstname,
#                                         last_name=registered_lastname,
#                                         email=registered_email)
#         user.save()
#         seller_profile = User.objects.create()
#         messages.success(request, "Your store has created!")
#         return redirect('/seller/products') 
#     else:  
#         form = FormRegistration()
#     return render(request, 'Sregister.html', {'form': form })

@login_required
def userprofile(request):
    return render(request, "profile.html", {})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        cust = Editprofile(request.POST, instance=user)
        if cust.is_valid():
            cust.save()
            messages.success(request, "updated success!")
            return redirect('Core:profile')
    else:
        cust = Editprofile(instance=user)
    context = {'cust': cust, }
    return render(request, 'edit_profile.html', context)