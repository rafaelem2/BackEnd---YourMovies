# Generated by Django 3.2.6 on 2021-11-14 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yourMovies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Favorite',
        ),
    ]
