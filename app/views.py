from django.shortcuts import render
from app.models import Post, Author
from django.urls import reverse

def index(request):
    latest_posts = Post.objects.all()[:5]

    for post in latest_posts:
        post.url  = reverse("post", args=[post.id])

    return render(request, "pages/home.html", {"latest_posts": latest_posts})

def post(request, post_id):
    post = Post.objects.get(id=post_id)

    post.author.url = reverse("author", args=[post.author.id])
    
    return render(request, "pages/article.html", {"post": post})

def author(request, author_id):
    author = Author.objects.get(id=author_id)

    return render(request, "pages/author.html", {"author": author})

