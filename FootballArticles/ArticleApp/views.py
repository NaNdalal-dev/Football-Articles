from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Official Views
def Official(request):
	data2 = OfficialArticle.objects.all()[::-1]
	data = data2
	title = 'Official • Football Articles'
	c1 = True
	return render(request, 'official.html',{'allData':data,'title':title,'c1':c1})

def OfficialWhole(request,link):
	try:
		c = 'c2'
		data = OfficialArticle.objects.get(id=link)
		data.Article = data.Article.split('\n')
		title = data.Title
		path = request.get_full_path()
		return render(request,'fullArticle.html',{'data':data,'path':path,'title':title,'c':c})
	except OfficialArticle.DoesNotExist:
		return render(request, 'errors/noArticle.html')
	except ValueError:
		return render(request, 'errors/noArticle.html')

# Transfers Views
def Transfers(request):
	data2 = TransfersArticle.objects.all()[::-1]
	data = data2
	title = 'Transfers • Football Articles'
	return render(request, 'Transfers.html',{'allData':data,'title':title})

def TransfersWhole(request,link):
	try:
		c = 'c3'
		data = TransfersArticle.objects.get(id=link)
		data.Article = data.Article.split('\n')
		path = request.get_full_path()
		title = data.Title
		return render(request,'fullArticle.html',{'data':data,'path':path,'title':title,'c':c})
	except TransfersArticle.DoesNotExist:
		return render(request, 'errors/noArticle.html')
	except ValueError:
		return render(request, 'errors/noArticle.html')

# HotTopic Views
def HotTopic(request):
	data2 = HotTopicArticle.objects.all()[::-1]
	data = data2
	title = 'HotTopic • Football Articles'
	return render(request, 'hottopic.html',{'allData':data,'title':title})

def HotTopicWhole(request,link):
	try:
		c = 'c1'
		data = HotTopicArticle.objects.get(id=link)
		data.Article = data.Article.split('\n')
		path = request.get_full_path()
		title = data.Title
		return render(request,'fullArticle.html',{'data':data,'path':path,'title':title,'c':c})
	except HotTopicArticle.DoesNotExist:
		return render(request, 'errors/noArticle.html')
	except ValueError:
		return render(request, 'errors/noArticle.html')


error404 = lambda request,exception: render(request,'404.html')