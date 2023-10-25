from django.urls import path
from me import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
     path('me', views.index, name='index'),
    ]                                                    
