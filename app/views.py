from django.http import HttpResponse
from django.shortcuts import render
from app.models import Post

def index(request):
    latest_posts = Post.objects.all()[:5]
    return render(request, "pages/home.html", {"latest_posts": latest_posts})

def tw(request):
    return render(request, "test/tw.html")