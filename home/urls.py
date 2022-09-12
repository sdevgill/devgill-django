from django.urls import path
from .views import HomePageView

# When using class-based views, we always add as_view() to the end of the view name
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
]


# FBV
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]
