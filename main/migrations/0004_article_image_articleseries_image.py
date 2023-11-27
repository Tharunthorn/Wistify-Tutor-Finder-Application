# Generated by Django 4.2 on 2023-11-25 18:20

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_article_author_articleseries_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default/no_image.jpg', max_length=255, upload_to=main.models.Article.image_upload_to),
        ),
        migrations.AddField(
            model_name='articleseries',
            name='image',
            field=models.ImageField(default='default/no_image.jpg', max_length=255, upload_to=main.models.ArticleSeries.image_upload_to),
        ),
    ]
