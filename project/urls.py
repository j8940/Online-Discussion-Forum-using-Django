
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.views.static import serve 
#from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('register.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    #path(r'^(?P<id>\d+)/$',views.update_post, name='update_post'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)