from django.views.generic import TemplateView

from blog.models import Post


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


# FBV
# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return render(request, "index.html")
