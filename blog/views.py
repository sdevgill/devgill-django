from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_post.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
