from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=30, unique=True)
    content = models.TextField(max_length=4000)
    # created_at calls when object creates very first time
    created_at = models.DateTimeField(auto_now_add=True)
    # update_at calls every time object saves
    updated_at = models.DateTimeField(auto_now=True)
    rubric = models.ForeignKey(
        "Rubric",
        related_name="articles",
        on_delete=models.PROTECT)
    author = models.ForeignKey(
        "Author",
        related_name="articles",
        on_delete=models.SET_NULL,
        null=True,
    )
    tags = models.ManyToManyField("Tag", related_name="articles")

    def get_absolute_url(self):
        return reverse("get_article_details", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.title} - {self.rubric.subject} - {self.author.name}"


class Rubric(models.Model):
    subject = models.CharField(max_length=30, unique=True)

    def get_absolute_url(self):
        return reverse("get_rubric_details", kwargs={"pk": self.id})

    def __str__(self):
        return f"Subject of Rubric: {self.subject} - {self.id}"


class Author(models.Model):
    name = models.CharField(max_length=40)
    occupation = models.CharField(max_length=30)
    email = models.EmailField()
    rubrics = models.ManyToManyField("Rubric", related_name="authors")

    def get_absolute_url(self):
        return reverse("get_author_details", kwargs={"pk": self.id})

    def __str__(self):
        return f"Author: {self.name} - {self.rubrics}"


class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)
    rubric = models.ForeignKey(
        "Rubric",
        related_name="tags",
        on_delete=models.SET_NULL,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("get_tag_details", kwargs={"pk": self.id})

    def __str__(self):
        return f"Tag title - {self.title}. Rubric - {self.rubric}"
