from django.urls import path
from .views import *


urlpatterns = [
	path('Official/',official,name='official')
]