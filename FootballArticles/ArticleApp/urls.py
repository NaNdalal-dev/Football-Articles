from django.urls import path, include
from .views import*
urlpatterns = [
	path('Transfers/',Transfers,name='transfers'),
	path('Transfers/<str:link>/',TransfersWhole,name='transferswhole'),
	
	path('Official/',Official,name='official'),
	path('Official/<str:link>/',OfficialWhole,name='OfficialWhole'),

	path('HotTopic/',HotTopic,name='hottop'),
	path('HotTopic/<str:link>/',HotTopicWhole,name='hottopWhole')
]