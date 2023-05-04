from django.contrib import admin
from django.urls import path,include
from . import views
from .views import Blogin, Blogout, category_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',views.Blogin,name="login"),
    path('categories/', views.category_list, name='category_list'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)