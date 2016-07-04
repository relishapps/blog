from django.conf.urls import patterns, url

from .views import Blog, BlogPost

urlpatterns = [
    url(r'^blog/$', Blog.as_view(), name='blog'),
    url(r'^blog/([a-z0-9-]+)/$', BlogPost.as_view(), name='blog_post')
]
