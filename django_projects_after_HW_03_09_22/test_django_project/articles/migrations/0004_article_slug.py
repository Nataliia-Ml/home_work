# Generated by Django 4.1 on 2022-09-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_author_rubrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=False,
        ),
    ]
