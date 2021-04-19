from django.urls import path, include
from .views import*
urlpatterns = [
	path('Transfers/',Transfers,name='transfers'),
	path('Official/',Official,name='official'),
	path('HotTopic/',HotTopic,name='hottop')
]