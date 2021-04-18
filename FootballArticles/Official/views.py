from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def official(request):
	return render(request, 'Official/OfficialArticalList.html')