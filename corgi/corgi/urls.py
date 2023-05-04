from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('seller/', include('seller.urls')),
    path('', include("homepage.urls")),
    path('store', include('buyer.urls')),
    path('buyer/', include('buyer.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)