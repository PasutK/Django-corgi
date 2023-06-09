from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path("register/", views.userregister, name='register'),
    path("login/", views.userlogin, name="login"),
    path("logout/", views.userlogout, name="logout"),
    path("", views.userprofile, name="login"),
    path("profile/", views.viewprofile, name="login"),
    path('edit-profile/', views.editUser_profile, name='edit_profile'),
    path('order_status/', views.order_status, name='order_status'),
]
