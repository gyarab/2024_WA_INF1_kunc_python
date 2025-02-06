from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world")

def tw(request):
    return render(request, 'test/tw.html')