from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
	return redirect('/HotTopic/')


def about(request):
	post = render(request,'about.html',{'title':'About'})
	return post

def server_error_handler (request,exception):
	if request.path.startswith('/HotTopic/') or request.path.startswith('/Official/') or request.path.startswith('/Transfers/'):
		return render(request,'505.html') 
		
error404 = lambda request,exception : render(request,'404.html')
