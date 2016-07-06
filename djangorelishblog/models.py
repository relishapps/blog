import re

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from markdownx.models import MarkdownxField

more_link_re = re.compile('\[\[ MORE_LINK \]\]', re.I)


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

    def unpublished(self):
        return self.filter(published=False)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = MarkdownxField()
    published = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    objects = PostQuerySet.as_manager()

    @property
    def intro(self):
        return more_link_re.split(self.body, 1)[0]

    @property
    def full_body(self):
        return more_link_re.sub('', self.body, 1)

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
