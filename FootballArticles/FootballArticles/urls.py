from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('about/',about,name='about'),
    path('',include('HotTopic.urls')),
    path('',include('Official.urls')),
    path('',include('Transfers.urls'))
]
