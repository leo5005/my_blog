from django.shortcuts import render,redirect
from http.client import HTTPResponse
from .models import Post
from blog.forms import CommentForm
from .forms import PostForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
          comment = form.save(commit=False)
          comment.post = post    
          comment.save()
          
          return redirect("post_detail",slug=post.slug)
    else:
        form = CommentForm()
        
    
    return render(request,"blog/post_detail.html",{"post": post,"form":form})

class CreatePostView(View):
    def get(self,request,*args,**kwargs):
        form = PostForm(request.POST or None)
        return render(request, "blog/post_form.html",{
            "form" : form
        })
        

