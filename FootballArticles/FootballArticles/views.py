from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
	return redirect('/HotTopic/')


def about(request):
	post = render(request,'about.html',{'title':'About'})
	return post

