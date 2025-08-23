from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings


def index(request):
    return render(request, 'index.html')


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('user.urls', namespace='user')),
    path('posts/', include('post.urls', namespace='post')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
