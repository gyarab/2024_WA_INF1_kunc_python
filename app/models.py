from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    expiryDate = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-createdAt"]


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
    
    class Meta:
        ordering = ["-createdAt"]


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    posts = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
