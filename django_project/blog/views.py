from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>About the Blog</h1>')