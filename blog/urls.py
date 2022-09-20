from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("new/", BlogCreateView.as_view(), name="blog_new"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="blog_post"),
]
