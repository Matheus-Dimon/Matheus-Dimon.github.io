from django.urls import URLPattern, path
from me import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.welcome, name='welcome'),
     path('me', views.index, name='index'),
    ]                                                    
