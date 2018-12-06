from django.db import models
from django.utils.text import slugify


# Create your models here.


class BlogPost(models.Model):
    """The model to save a blog page. 
    The body is saved as markdown. tags are implemented via taggit. authors is form users. 
    subtitle is the plain text 2 sentence description about the blog.
    """
    title = models.CharField(max_length=300)
    subtitle = models.TextField()
    body = models.TextField()
    slug = models.CharField(max_length=350, unique=True, blank=True, default='')  # enforced in save

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """over ride the save to auto-generate the slug, if it's not already provided"""
        if self.slug == '':
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
