# Generated by Django 4.2 on 2023-11-27 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_articleseries_series_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleseries',
            name='series_rating',
        ),
    ]
