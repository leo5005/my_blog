from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField("タイトル", max_length=255,
    blank=True,
    null=False)
    
    content = models.Textfield("本文")
    
    slug = models.SlugField()
    intro = models.TextField()
    
    body = models.TextField(
    blank=True,
    null=False)
    
    posted_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default=timezone.now)
    
    
class Category(models.Model):
    name = models.CharField(
    max_length = 255,
    blank = False,
    null = False,
    unique = True)
 
class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()     
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
        
    
    