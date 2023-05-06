from django.contrib import admin
from django.urls import path,include
from . import views
from .views import Blogin, Blogout, category_detail, product_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Bhomepage,name="login"),
    path('login',views.Blogin,name="login"),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category>/', views.category_detail, name='category_detail'),
    path('categories/<int:category>/<str:name>/', views.product_detail, name='product_detail'),
    path('store/<str:store_name>/', views.store_detail, name='store_detail'),
    path('cart/', views.cart, name='cart'),
    # path('cart/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/add_to_cart/checkout', views.checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


