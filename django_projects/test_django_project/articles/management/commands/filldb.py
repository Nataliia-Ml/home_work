import random

from django.core.management import BaseCommand
from faker import Faker

from articles.management.commands._common import rubrics_with_tags
from articles.models import (
    Article,
    Tag,
    Author,
    Rubric,
)


class Command(BaseCommand):
    help = "This command fill DB with mocked data"

    def handle(self, *args, **options):
        self.stdout.write("Fill DB start")
        self.clear_tables()
        self.create_rubrics_tags()
        self.create_authors()
        self.create_articles()
        self.stdout.write("Fill DB done")

    def clear_tables(self):
        self.stdout.write("Clear table from data")
        for model in (Article, Tag, Author, Rubric):
            model.objects.all().delete()

    def create_rubrics_tags(self):
        self.stdout.write("Create Rubrics and Tags")
        for rubric, tags in rubrics_with_tags.items():
            rubric = Rubric.objects.create(subject=rubric)
            tags_objects = [Tag(title=tag, rubric=rubric) for tag in tags]
            Tag.objects.bulk_create(tags_objects)

    def create_authors(self):
        self.stdout.write("Create Authors")
        faker = Faker()
        for _ in range(10):
            Author.objects.create(name=faker.name(), occupation=faker.job(), email=faker.email())

    def create_articles(self):
        self.stdout.write("Create Articles")
        all_authors = list(Author.objects.all())
        while all_authors:
            author: Author = all_authors.pop()
            faker = Faker()
            all_rubric = Rubric.objects.all()
            for _ in range(3):
                random_rubric: Rubric = random.choice(all_rubric)
                all_tags_in_rubric = random_rubric.tags.all()
                random_tag: Tag = random.choice(all_tags_in_rubric)
                article = Article.objects.create(
                    title=faker.text(max_nb_chars=20),
                    content=faker.paragraph(),
                    rubric=random_rubric,
                    author=author,
                )
                article.tags.add(random_tag)
