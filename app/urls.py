from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>/", views.post, name="post"),
    path("author/<int:author_id>/", views.author, name="author"),
]