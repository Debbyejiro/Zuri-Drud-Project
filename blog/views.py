from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Post, Comment


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
    posts = get_object_or_404(id=post_id)
    comments = posts.comments.all().order_by('-date_created')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=Post, user=request.user, content=content)
            comment.post = Post
            comment.save()
            return redirect(Post.get_absolute_urls())
    else:
        comment_form = CommentForm()
    context = {
        'post': Post,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'blog/details.html', context)


def add_new(request):
    form = CommentForm(request.POST or None)