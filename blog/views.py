from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Saurav Jalui',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'Feb 05, 2021',
    },
    {
        'author' : 'Ram Yadav',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'Feb 06, 2021',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
