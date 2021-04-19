from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('about/',about,name='about'),
    path('',include('ArticleApp.urls')),
    path('',include('ArticleApp.urls')),
    path('',include('ArticleApp.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )