from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),

    path("rubrics/", views.get_rubrics, name="get_all_rubrics"),
    path("rubric/<slug:slug>", views.get_rubric, name="get_rubric_details"),

    path("tags/", views.all_tags, name="get_all_tags"),
    path("tag/<slug:slug>", views.get_tag, name="get_tag_details"),

    path("authors/", views.all_authors, name="get_all_authors"),
    path("author/<slug:slug>", views.get_author, name="get_author_details"),

    path("articles/", views.get_articles, name="get_all_articles"),
    path("article/<slug:slug>", views.get_article, name="get_article_details"),
]