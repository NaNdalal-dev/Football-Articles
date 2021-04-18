from django.urls import path
from .views import *


urlpatterns = [
	path('HotTopic/',HotTopic,name='hottop')
]