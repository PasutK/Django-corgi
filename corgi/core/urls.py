from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    # path("register/", UserRegisterView.as_view(), name='register'),
    path("register/", views.userregister, name='register'),
    path("login/", views.userlogin, name="login"),
    path("logout/", views.userlogout, name="logout"),
    path("profile/", views.userprofile, name="login"),
    path('edit_profile/', views.editUser_profile, name='edit_profile'),
]
