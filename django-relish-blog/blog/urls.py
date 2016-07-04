from django.conf.urls import patterns, url

from .views import Blog, BlogPost

urlpatterns = patterns('',
    url(r'^$', Blog.as_view(), name='blog'),
    url(r'^([a-z0-9-]+)/$', BlogPost.as_view(), name='blog_post')
)
