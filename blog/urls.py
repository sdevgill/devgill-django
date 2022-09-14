from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    # path("post/<int:pk>/", BlogDetailView.as_view(), name="blog_post"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="blog_post"),
    path("", BlogListView.as_view(), name="blog"),
]
