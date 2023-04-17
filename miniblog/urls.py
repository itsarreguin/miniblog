from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings


urlpatterns = [
    path('', include('core.urls')),
    path('', include('posts.urls')),
    path('unicorn/', include('django_unicorn.urls'))
]

if settings.DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]