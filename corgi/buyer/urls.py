from django.contrib import admin
from django.urls import path,include
from . import views
from .views import Blogin, Blogout, category_list, category_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'buyer'

urlpatterns = [
    path('login',views.Blogin,name="login"),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


