from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    # BlogDeleteView,
)
from . import views

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("new/", BlogCreateView.as_view(), name="blog_new"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="blog_post"),
    path("<slug:slug>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    # path("<slug:slug>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    # FBV
    path("<slug:slug>/delete/", views.blog_delete, name="blog_delete"),
]
