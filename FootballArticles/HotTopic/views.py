from django.shortcuts import render
from django.http import HttpResponse


def HotTopic(request):
	return render(request, 'HotTopic/HotTopicArticleList.html')