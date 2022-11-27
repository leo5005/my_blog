from django.shortcuts import render
from http.client import HTTPResponse

def frontpage(request):
    return render(request, "blog/frontpage.html")


