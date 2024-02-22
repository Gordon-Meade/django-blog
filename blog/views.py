# blog/views.py

from django.http import HttpResponse
from django.shortcuts import render

def my_blog(request):
    return HttpResponse("Hello, Blog!")
