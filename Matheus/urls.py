from django.contrib import admin
from django.urls import include, path
from Matheus import settings
import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('me.urls')),  
]

