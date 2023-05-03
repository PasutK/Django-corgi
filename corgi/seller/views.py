from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
# Create your views here.
class Homepage(View):
    def get(self, request):
        return render(request, 'Shomepage.html', {})
    
class Register(View):
    def get(self, request):
        return render(request, 'Sregister.html', {})
    
def login_seller(request):
    return render(request, 'Slogin.html', {})

def logout_seller(request):
    return render(request, 'Slogout.html', {})