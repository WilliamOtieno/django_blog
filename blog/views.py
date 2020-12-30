from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

"""def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name='blog/home.html', context=context)"""


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about(request):
    return render(request, template_name='blog/about.html', context={'title': 'About'})
