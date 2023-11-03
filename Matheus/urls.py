from django.contrib import admin
from django.urls import include, path
from Matheus import settings
import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('me.urls')),  
]

+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)