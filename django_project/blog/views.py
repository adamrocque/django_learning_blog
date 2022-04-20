from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': "AdamR",
        'title': "Blog Post 1",
        'content': 'First post content',
        'date_posted': "August 27 2022"

    },
    {
        'author': "Sarah C",
        'title': "Blog Post 2",
        'content': 'Second post content',
        'date_posted': "August 28 2022"

    }
]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

