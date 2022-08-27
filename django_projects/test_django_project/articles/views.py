from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from articles.models import (
    Rubric,
    Tag,
    Author,
    Article,
)


def home(request: HttpRequest):
    all_models = {"Article": "all_articles/", "Rubric": "rubrics/", "Author": "authors/", "Tag": "tags/"}
    context = {"title": "Home", "models": all_models}
    return render(request, template_name="articles/home.html", context=context)


def all_rubrics(request: HttpRequest):
    rubrics = Rubric.objects.all()
    context = {"title": "Rubrics", "rubrics": rubrics}
    return render(request, template_name="articles/rubrics.html", context=context)


def get_rubric(request: HttpRequest, pk):
    rubric = Rubric.objects.get(pk=pk)
    return HttpResponse(f"Mocked Page for Rubric: {rubric}")


def all_tags(request: HttpRequest):
    tags = Tag.objects.all()
    context = {"title": "Tags", "tags": tags}
    return render(request, template_name="articles/tags.html", context=context)


def get_tag(request: HttpRequest, pk):
    tag = Tag.objects.get(pk=pk)
    return HttpResponse(f"Mocked Page for Tag: {tag}")


def all_authors(request: HttpRequest):
    authors = Author.objects.all()
    context = {"title": "Authors", "authors": authors}
    return render(request, template_name="articles/authors.html", context=context)


def get_author(request: HttpRequest, pk):
    author = Author.objects.get(pk=pk)
    return HttpResponse(f"Mocked Page for Author: {author}")


def all_articles(request: HttpRequest):
    articles = Article.objects.all()
    context = {"title": "Articles", "articles": articles}
    return render(request, template_name="articles/articles.html", context=context)


def get_articles(request: HttpRequest, pk):
    article = Article.objects.get(pk=pk)
    return HttpResponse(f"Mocked Page for Article: {article}")
