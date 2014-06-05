from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    title = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField(default=datetime.now)
    text = models.TextField(default="")
    slug = models.SlugField(max_length=40, unique=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]
