import re

from django.db import models
from django.conf import settings
from django.contrib import admin
from django.core.urlresolvers import reverse

more_link_re = re.compile('\[\[ *MORE_LINK *]]', re.I)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    published = models.BooleanField()

    @property
    def intro(self):
        return more_link_re.split(self.body, 1)[0]

    @property
    def full_body(self):
        return more_link_re.sub('', self.body, 1)

    @property
    def url(self):
        return reverse('blog_post', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author_name = models.CharField(max_length=64)
    author_email = models.EmailField()
    author_website = models.URLField(blank=True, null=True)
    body = models.TextField()


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
