import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import View, DetailView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from articles.models import (
    Rubric,
    Tag,
    Author,
    Article,
)


class RubricList(ListView):

    model = Rubric
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f"Context: {context}")
        print(f"Page kwargs: {self.page_kwarg}")
        print(f"Template Name: {self.get_template_names()}")

        context["title"] = "Rubrics List"
        return context


class ArticlesList(ListView):
    model = Article
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(f"Context: {context}")
        context["title"] = "Articles List"
        return context


class RubricDetail(DetailView):
    model = Rubric

    template_name = "articles/rubric_detail.html"

    def get_context_object_name(self, obj):
        return "rubric_detail"

    queryset = Rubric.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print(f"Context: {context}")
        context["title"] = f"Rubric | {context['rubric_detail'].subject}"
        print(f"Context: {context}")
        return context


def get_article(request: HttpRequest, slug):
    article = Article.objects.get(slug=slug)
    return HttpResponse(f"Mocked Page for Article: {article}")


def home(request: HttpRequest):
    all_models = {"Article": "articles/", "Rubric": "rubrics/", "Author": "authors/", "Tag": "tags/"}
    context = {"title": "Home", "models": all_models}
    return render(request, template_name="articles/home.html", context=context)


def all_tags(request: HttpRequest):
    tags = Tag.objects.all()
    context = {"title": "Tags", "tags": tags}
    return render(request, template_name="articles/tags.html", context=context)


def get_tag(request: HttpRequest, slug):
    tag = Tag.objects.get(slug=slug)
    return HttpResponse(f"Mocked Page for Tag: {tag}")


def all_authors(request: HttpRequest):
    authors = Author.objects.all()
    context = {"title": "Authors", "authors": authors}
    return render(request, template_name="articles/authors.html", context=context)


def get_author(request: HttpRequest, slug):
    author = Author.objects.get(slug=slug)
    return HttpResponse(f"Mocked Page for Author: {author}")

