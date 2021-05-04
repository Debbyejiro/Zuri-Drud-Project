from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Post, Comments


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


def details(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all().order_by('-date_created')

    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            content = request.POST.get('content')
            comment = Comments.objects.create(post=post, user=request.user, content=content)
            comment.post = post
            comment.save()
            return redirect(Post.get_absolute_urls())
    else:
        cf = CommentForm()
    context = {
        'post': post,
        'comment_form': cf,
        'comments': comments,
    }

    return render(request, 'blog/details.html', context)


def add_new(request):
    form = CommentForm(request.POST or None)