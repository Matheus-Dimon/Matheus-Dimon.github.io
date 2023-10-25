from django.urls import path
from me import views


urlpatterns = [
    path('', views.index, name='index'),
    ]                                                    
