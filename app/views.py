from django.shortcuts import render
from app.models import Post, Tag, Comment
from django.urls import reverse
from .lib.color_calc import calculate_expiry_color
from django.http import JsonResponse
from app.forms import CommentForm, RegistrationForm, LoginForm
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.db import models

def _register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        User = get_user_model()
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)


        return redirect(reverse("index"))

    return render(request, "pages/register.html", {"form": RegistrationForm()})


def _login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User = get_user_model()
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=403)

    return render(request, "pages/login.html", {"form": LoginForm()})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)

    return redirect(reverse("index"))
    
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

    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "You must be logged in to comment"}, status=403)

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_obj = Post.objects.get(id=post_id)
            comment = Comment()
            comment.post = post_obj
            comment.author = request.user
            comment.content = comment_form.cleaned_data["content"]
            comment.save()

    post = Post.objects.select_related('author').prefetch_related('tags').prefetch_related(
        "comments__author"
    ).get(id=post_id)
    post.author.url = reverse("author", args=[post.author.id])
    post.expiry_color = calculate_expiry_color(post.expires_at)
    post.tag_names = [tag.name for tag in post.tags.all()]
    post.comment_list = post.comments.select_related('author').all()
    form = CommentForm()

    print(post.comment_list[0].author)
    
    return render(request, "pages/article.html", {"post": post, "form": form})

def authors(request):
    posts = Post.objects.select_related('author').all()
    authors = set(post.author for post in posts if post.author is not None)

    for author in authors:
        author.url = reverse("author", args=[author.id])
        author.post_count = posts.filter(author=author).count()
        random_post = posts.filter(author=author).order_by('?').first()
        author.random_post = random_post
        if random_post:
            author.random_post.url = reverse("post", args=[random_post.id])

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

def meta(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    remote_addr = request.META.get('REMOTE_ADDR')

    user_agent = request.META.get('HTTP_USER_AGENT', '')

    uuid_cookie = request.COOKIES.get('uuid')

    return JsonResponse({"forwarded_for": forwarded_for, "remote_addr": remote_addr, "user_agent": user_agent, "uuid_cookie": uuid_cookie})
