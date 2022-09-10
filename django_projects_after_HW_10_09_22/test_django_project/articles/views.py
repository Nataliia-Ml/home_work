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


# def get_rubrics(request: HttpRequest):
#     rubrics = Rubric.objects.all()
#     context = {"title": "Rubrics", "rubrics": rubrics}
#     return render(request, template_name="articles/rubric_list.html", context=context)


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

    # QuerySet ->
    #   Manager (Rubric.objects)
    #   or
    #   Queryset(Rubric.objects.all())
    # 1 step
    queryset = Rubric.objects.all()

    # 2 step
    def get_queryset(self):
        # return self.queryset.filter(slug=self.kwargs.get("slug"))
        return super().get_queryset()

    # 3 step
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print(f"Context: {context}")
        context["title"] = f"Rubric | {context['rubric_detail'].subject}"
        print(f"Context: {context}")
        return context


# def get_rubric(request: HttpRequest, slug):
#     rubric = Rubric.objects.get(slug=slug)
#     return HttpResponse(f"Mocked Page for Rubric: {rubric}")


# @method_decorator(csrf_exempt, name='dispatch')
# class RubricDetail(View):
#
#     def get(self, request, *args, **kwargs):
#         print(f"args: {args}, kwargs: {kwargs}")
#         return render(request, template_name="articles/rubric_detail.html")

    # def post(self, request, *args, **kwargs):
        # print(f"args: {args}, kwargs: {kwargs}")
        # return render(request, template_name="articles/rubric_detail.html")

        # # The request.body is bynary string. We need to decode (for python <3.5) and load.
        # body_binary: bytes = request.body
        #
        # # Only for Python < 3.5
        # body_str = body_binary.decode("UTF-8")
        #
        # body_dict: dict = json.loads(body_str)
        # print(f"Body as Python object {type(body_dict)}: {body_dict}")
        #
        # # Creating author from body:
        # author = Author.objects.create(**body_dict)
        # return HttpResponse({author})


# def get_articles(request: HttpRequest):
#     articles = Article.objects.all()
#     context = {"title": "Articles", "articles": articles}
#     return render(request, template_name="articles/article_list.html", context=context)


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

