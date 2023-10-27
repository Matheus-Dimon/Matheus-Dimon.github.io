from django.urls import URLPattern, path
from me import views
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    URLPattern += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('', views.welcome, name='welcome'),
     path('me', views.index, name='index'),
    ]                                                    
