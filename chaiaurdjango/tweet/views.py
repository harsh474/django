from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def tweet(request): 
     # return HttpResponse("hi this is a tweet app")
     return render(request,'index.html')

