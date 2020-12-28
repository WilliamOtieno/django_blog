from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'William JO',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '28th Dec 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '29th Dec 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    return render(request, template_name='blog/about.html', context={'title': 'About'})
