from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey("Author", related_name="book", on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey("Publisher", related_name="book", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Title: '{self.title}'. Author: {self.author}. Publisher: {self.publisher}."


class Author(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    rating = models.FloatField()

    def __str__(self):
        return f"Author {self.full_name} - {self.email}. Rating={str(self.rating)}"


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"Publishers {self.name}, {self.address}. Website: {self.url}"
