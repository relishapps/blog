from django.conf.urls import url

from .views import Blog, BlogPost

urlpatterns = [
    url(r'^$', Blog.as_view(), name='blog'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', BlogPost.as_view(), name='blog_post')
]
