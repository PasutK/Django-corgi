from django.contrib import admin
from django.urls import path,include
from . import views
from .views import Blogin, Blogout, product_detail, product_category
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Bhomepage,name="login"),
    path('login',views.Blogin,name="login"),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.product_category, name='category_detail'),
    # path('categories/<int:pk>/<int:pd>/', views.product_detail, name='product_detail'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


