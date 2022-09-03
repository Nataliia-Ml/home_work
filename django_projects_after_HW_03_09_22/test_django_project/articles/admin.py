from django import forms
from django.contrib.admin import register, ModelAdmin

from articles.models import (
    Article,
    Author,
    Tag,
    Rubric,
)


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['slug', ]


@register(Article)
class ArticleAdmin(ModelAdmin):
    form = ArticleAdminForm
    list_display = ("title", "author", "created_at")
    list_filter = ("rubric", )
    search_fields = ("content__contains",)


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['slug', ]


@register(Author)
class AuthorAdmin(ModelAdmin):
    form = AuthorAdminForm
    list_display = ("name", "occupation", "email", )
    list_filter = ("rubrics", )
    search_fields = ("name__contains",)


class RubricAdminForm(forms.ModelForm):
    class Meta:
        model = Rubric
        exclude = ['slug', ]


@register(Rubric)
class RubricAdmin(ModelAdmin):
    form = RubricAdminForm
    list_display = ("subject", )


class TagAdminForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ['slug', ]


@register(Tag)
class TagAdmin(ModelAdmin):
    form = TagAdminForm
    list_display = ("title", "rubric",)
