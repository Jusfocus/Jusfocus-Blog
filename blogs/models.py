from django.db import models

# Create your models here.


class BlogPage(models.Model):
    """The model to save a blog page. 
    The body is saved as markdown. tags are implemented via taggit. authors is form users. 
    subtitle is the plain text 2 sentence description about the blog.
    """
    title = models.CharField(max_length=300)
    subtitle = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
