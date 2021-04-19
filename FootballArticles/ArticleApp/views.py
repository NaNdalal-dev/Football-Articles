from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Official Views
def Official(request):
	data2 = OfficialArticle.objects.all().order_by('Time')[::-1]
	data = data2
	return render(request, 'official.html',{'allData':data})

def OfficialWhole(request,link):
	data = OfficialArticle.objects.get(id=link)
	data.Article = data.Article.split('\n')
	return render(request,'fullArticle.html',{'data':data})

# Transfers Views
def Transfers(request):
	data2 = TransfersArticle.objects.all().order_by('Date')[::-1]
	data = data2
	return render(request, 'Transfers.html',{'allData':data})

def TransfersWhole(request,link):
	data = TransfersArticle.objects.get(id=link)
	data.Article = data.Article.split('\n')
	return render(request,'fullArticle.html',{'data':data})

# HotTopic Views
def HotTopic(request):
	data2 = HotTopicArticle.objects.all().order_by('Time')[::-1]
	data = data2
	return render(request, 'hottopic.html',{'allData':data})

def HotTopicWhole(request,link):
	data = HotTopicArticle.objects.get(id=link)
	data.Article = data.Article.split('\n')
	return render(request,'fullArticle.html',{'data':data})