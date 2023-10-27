from ast import pattern
from django.contrib import admin
from django.urls import include, path
from Matheus import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('me.urls')),  
]

if not settings.DEBUG:
    urlpatterns += pattern('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
