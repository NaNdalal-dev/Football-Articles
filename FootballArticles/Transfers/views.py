from django.shortcuts import render
from django.http import HttpResponse

def transfers(request):
	return render(request,'Transfers/TransfersArticalList.html')