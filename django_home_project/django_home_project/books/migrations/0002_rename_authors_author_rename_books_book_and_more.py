# Generated by Django 4.1 on 2022-08-16 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Publishers',
            new_name='Publisher',
        ),
    ]