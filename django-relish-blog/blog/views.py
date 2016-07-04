from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.base import View
from django.template import RequestContext

from .models import Post


class Blog(View):
    def get(self, request):
        if request.user.is_authenticated():
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(published=True)

        return render_to_response('templates/index.html', {'posts': posts}, context_instance=RequestContext(request))


class BlogPost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        return render_to_response('templates/post.html', {'post': post}, context_instance=RequestContext(request))
