from django.urls import URLPattern, path
from me import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.welcome, name='welcome'),
     path('me', views.index, name='index'),
    ]                                                    

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)