from django.urls import path, include
from . import views
from .views import *
from django.conf.urls.static import static


urlpatterns = [
    path('', views.sbase,name='seller-homepage'),
    path('register/', views.register_seller,name='seller-register'),
    path('products/', views.seller_product, name='seller_product'),
    path('products/<str:sellerproduct>/', views.sproduct_detail, name='sproduct_detail'),
    path('add-products/', views.add_product, name='add_product'),
    path('edit-products/<int:id>/', views.edit_product, name='edit_product'),
    path('store-profile/', views.store_profile, name='store_profile'),
    path('store-profile/edit-profile/', views.edit_store, name='edit_profile'),
    path('order-status/', views.order_status, name='order_status'),
    # path('delete-products/', views.delete_products, name='delete_products'),
    path('payment-overview/', views.order_status, name='order_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)