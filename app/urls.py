from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authors/", views.authors, name="authors"),
    path("tags/", views.tags, name="tags"),
    path("post/<int:post_id>/", views.post, name="post"),
    path("author/<int:author_id>/", views.author, name="author"),
    path("tag/<int:tag_id>/", views.tag, name="tag"),
]