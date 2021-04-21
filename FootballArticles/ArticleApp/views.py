from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Official Views
def recentArticles(currentID):
	AList = ArticleAttributes.objects.all()[::-1]
	i = 0
	articles = []
	for article in AList:
		if i > 4:
			break
		if article.id != currentID:
			articles.append(article)
		i += 1
	return articles



def Official(request):
	data2 = OfficialArticle.objects.all()[::-1]
	data = data2
	return render(request, 'official.html',{'allData':data})

def OfficialWhole(request,link):
	data = OfficialArticle.objects.get(id=link)
	data.Article = data.Article.split('\n')
	recent = recentArticles(data.id)
	return render(request,'fullArticle.html',{'data':data,'recent':recent})

# Transfers Views
def Transfers(request):
	data2 = TransfersArticle.objects.all()[::-1]
	data = data2
	return render(request, 'Transfers.html',{'allData':data})

def TransfersWhole(request,link):
	data = TransfersArticle.objects.get(id=link)
	data.Article = data.Article.split('\n')
	recent = recentArticles(data.id)
	return render(request,'fullArticle.html',{'data':data,'recent':recent})

# HotTopic Views
def HotTopic(request):
	data2 = HotTopicArticle.objects.all()[::-1]
	data = data2
	return render(request, 'hottopic.html',{'allData':data})

def HotTopicWhole(request,link):
	data = HotTopicArticle.objects.get(id=link)
	data.Article = data.Article.split('\n')
	recent = recentArticles(data.id)
	return render(request,'fullArticle.html',{'data':data,'recent':recent})