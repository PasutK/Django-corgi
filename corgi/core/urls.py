from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    # path("register/", UserRegisterView.as_view(), name='register'),
    path("register/", views.userregister, name='register'),
    path("login/", views.userlogin, name="login"),
    path("logout/", views.userlogout, name="logout"),
    path("", views.userprofile, name="login"),
    path("profile/", views.viewprofile, name="login"),
    path('edit-profile/', views.editUser_profile, name='edit_profile'),
    path('order_status/', views.editUser_profile, name='edit_profile'),
]
