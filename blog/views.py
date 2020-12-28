from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'William JO',
        'title': 'blog post 1',
        'content': 'first post content',
        'data_posted': '28th Dec 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog post 2',
        'content': 'second post content',
        'data_posted': '29th Dec 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    return render(request, template_name='blog/about.html')
