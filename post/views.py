from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Post
# from django.urls import
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView


# Create your views here.
def hello(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/htmltag.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


def post_detail(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'post/post_detail.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail2.html'
    context_object_name = 'post'


def greet(request):
    return HttpResponse("Hi")


def eat(request):
    return HttpResponse("Chop 🍴")


def htmlTag(request):
    return render(request, 'htmltag.html')


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_new.html'
    fields = ['title', 'body', 'author']
    # success_url = 'home'
    success_url = reverse_lazy('home2')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home2')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_edit.html'
    fields = ['title', 'body']
