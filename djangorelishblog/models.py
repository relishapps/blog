from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from markdownx.models import MarkdownxField


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

    def unpublished(self):
        return self.filter(published=False)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    intro = MarkdownxField()
    body = MarkdownxField()
    published = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    objects = PostQuerySet.as_manager()

    def content(self):
        return '%s\n\n%s' % (self.intro, self.body)

    @property
    def url(self):
        return reverse('blog_post', args=[self.slug])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author_name = models.CharField(max_length=64)
    author_email = models.EmailField()
    author_website = models.URLField(blank=True, null=True)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return '%s on %s' % (self.author_name, self.created_on)
