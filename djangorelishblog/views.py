from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.template import RequestContext

from .models import Post


class Blog(ListView):
    model = Post
    template_name = 'djangorelishblog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self, request):
        if request.user.is_authenticated():
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(published=True)

        return posts


class BlogPost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        return render(request, 'djangorelishblog/post.html', {'post': post}, RequestContext(request))
