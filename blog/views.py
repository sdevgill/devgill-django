from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_post.html"


class BlogCreateView(CreateView):
    model = Post
    fields = (
        "title",
        "body",
        "slug",
    )
    template_name = "blog_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    fields = (
        "title",
        "body",
        "slug",
    )
    template_name = "blog_edit.html"


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blog")
