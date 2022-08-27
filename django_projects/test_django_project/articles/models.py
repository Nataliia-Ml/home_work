from django.db import models


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

    def __str__(self):
        return f"{self.title} - {self.content} - {self.rubric} - {self.author} - {self.tags}"


class Rubric(models.Model):
    subject = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"Subject of Rubric: {self.subject} "


class Author(models.Model):
    name = models.CharField(max_length=40)
    occupation = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Author: {self.name} - {self.occupation} - {self.email}"


class Tag(models.Model):
    title = models.CharField(max_length=30, unique=True)
    rubric = models.ForeignKey(
        "Rubric",
        related_name="tags",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"Tag title - {self.title}. Rubric - {self.rubric}"
