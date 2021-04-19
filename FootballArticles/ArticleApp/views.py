from django.shortcuts import render
from django.http import HttpResponse
from .models import*

# Create your views here.
def Official(request):
	return render(request, 'official.html')

def Transfers(request):
	data2 = TransfersArticle.objects.get
	data = data2()
	data.Article = data.Article.split('\n')
	print(data.Article)
	return render(request, 'Transfers.html',{'data':data})

def HotTopic(request):
	return render(request, 'hottopic.html')
