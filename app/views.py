from django.shortcuts import render
from app.models import Post, Author, Tag
from django.urls import reverse

from .lib.color_calc import calculate_expiry_color
from django.http import JsonResponse

def index(request):
    latest_posts = Post.objects.select_related('author').prefetch_related('tags').all()[:5]
    expiring_posts = Post.objects.select_related('author').prefetch_related('tags').filter(expires_at__isnull=False).order_by("expires_at")[:5]
    

    for post in latest_posts:
        post.url = reverse("post", args=[post.id])
        post.tag_names = [tag.name for tag in post.tags.all()]
        post.expiry_color = calculate_expiry_color(post.expires_at)

    for post in expiring_posts:
        post.url = reverse("post", args=[post.id])
        post.tag_names = [tag.name for tag in post.tags.all()]
        post.expiry_color = calculate_expiry_color(post.expires_at)


    return render(request, "pages/home.html", {"latest_posts": latest_posts, "expiring_posts": expiring_posts})

def post(request, post_id):
    post = Post.objects.select_related('author').prefetch_related('tags').prefetch_related("comments").get(id=post_id)
    post.author.url = reverse("author", args=[post.author.id])
    post.expiry_color = calculate_expiry_color(post.expires_at)
    post.tag_names = [tag.name for tag in post.tags.all()]
    post.comment_list = post.comments.all()
    
    return render(request, "pages/article.html", {"post": post})

def authors(request):
    authors = Author.objects.all().prefetch_related("post_set")

    for author in authors:
        author.url = reverse("author", args=[author.id])
        author.post_count = author.post_set.count()
        author.random_post = author.post_set.order_by('?').first()
        author.random_post.url = reverse("post", args=[author.random_post.id])

    return render(request, "pages/authors.html", {"authors": authors})

def tags(request):
    tags = Tag.objects.all().prefetch_related("post_set")

    for tag in tags:
        tag.url = reverse("tag", args=[tag.id])
        tag.post_count = tag.post_set.count()
        tag.random_post = tag.post_set.order_by('?').first()
        tag.random_post.url = reverse("post", args=[tag.random_post.id])

    return render(request, "pages/tags.html", {"tags": tags})

def author(request, author_id):
    return JsonResponse({"error": "Not found"}, status=404)

def tag(request, tag_id):
    return JsonResponse({"error": "Not found"}, status=404)
