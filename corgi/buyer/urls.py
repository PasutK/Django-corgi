from django.contrib import admin
from django.urls import path,include
from . import views
from .views import Blogin, Blogout

urlpatterns = [
    path('login',views.Blogin,name="login"),
]
