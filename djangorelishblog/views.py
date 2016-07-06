from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.template import RequestContext

from .models import Post, Comment
from .forms import CommentForm


class Blog(ListView):
    model = Post
    template_name = 'djangorelishblog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.published()


class BlogPost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        comment_form = CommentForm()

        return render(request, 'djangorelishblog/post.html', {'post': post, 'comment_form': comment_form}, RequestContext(request))

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog_post', kwargs={'slug': slug})

        return render(request, 'djangorelishblog/post.html', {'post': post, 'comment_form': comment_form}, RequestContext(request))
