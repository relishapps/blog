from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.template import RequestContext

from .models import Post


class Blog(View):
    def get(self, request):
        if request.user.is_authenticated():
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(published=True)

        return render(request, 'djangorelishblog/blog.html', {'posts': posts}, RequestContext(request))


class BlogPost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        return render(request, 'djangorelishblog/post.html', {'post': post}, RequestContext(request))
