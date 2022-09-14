from django.urls import path
from .views import HomePageView, AboutPageView

# When using class-based views, we always add as_view() to the end of the view name
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("about/", AboutPageView.as_view(), name="about"),
]


# FBV
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]
