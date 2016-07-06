from django.conf.urls import url

from .views import BlogView, BlogPostView

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', BlogPostView.as_view(), name='blog_post')
]
