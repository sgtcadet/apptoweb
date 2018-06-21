from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('Index view func calling')
    return render(request,'index.html')