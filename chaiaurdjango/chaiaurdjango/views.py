from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello, Django! i am Harsh Rajput")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("Hello, Django! i am About")
def car(request):
    return HttpResponse("Hello, Django! i am car")
def bus(request):
    return HttpResponse("Hello, Django! i am Harsh Rajput bus")