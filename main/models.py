from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import os


class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)
    subjects = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None


    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    article_slug = models.SlugField("Article slug", null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default="")
    notes = HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)
    total_rating = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def update_total_rating(self):
        # Calculate and update the total rating based on comments
        comments = self.comments.all()
        if comments.exists():
            total_rating = sum(comment.rating for comment in comments) / comments.count()
            self.total_rating = total_rating
            self.save()


    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    # Add other necessary fields like timestamp, etc.

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.article.update_total_rating()

