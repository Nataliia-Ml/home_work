from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),

    path("rubrics/", views.all_rubrics, name="get_all_rubrics"),
    path("rubric/<int:pk>", views.get_rubric, name="get_rubric_details"),

    path("tags/", views.all_tags, name="get_all_tags"),
    path("tag/<int:pk>", views.get_tag, name="get_tag_details"),

    path("authors/", views.all_authors, name="get_all_authors"),
    path("author/<int:pk>", views.get_author, name="get_author_details"),

    path("all_articles/", views.all_articles, name="get_all_articles"),
    path("article/<int:pk>", views.get_articles, name="get_article_details"),
]
