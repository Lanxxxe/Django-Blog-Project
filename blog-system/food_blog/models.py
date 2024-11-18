from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    username = models.CharField(max_length=100, default='Anonymouse User')  # Updated field
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.username} on {self.post}'








