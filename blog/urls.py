from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import settings

urlpatterns = [
                  path('', include('home.urls')),
                  path('post/', include('post.urls')),
                  path('admin/', admin.site.urls),
                  path('summernote/', include('django_summernote.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
