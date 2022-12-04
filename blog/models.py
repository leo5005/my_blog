from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(
    max_length=255,
    blank=True,
    null=False)
    
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
 
def __str__(self):
    return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
        
    
    