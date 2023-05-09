from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.sbase,name='seller-homepage'),
    path('register/', views.register_seller,name='seller-register'),
    path('products/', views.seller_product, name='seller_product'),
    path('products/<str:sellerproduct>/', views.sproduct_detail, name='sproduct_detail'),
    path('add-products/', views.add_product, name='add_product'),
    path('edit-products/<int:id>/', views.edit_product, name='edit_product'),
    path('edit-profile/', views.edit_seller, name='edit_profile'),

    # path('delete-products/', views.delete_products, name='delete_products'),
]
