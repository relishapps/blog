from django.contrib import admin
from .models import Post, Comment
from markdownx.admin import MarkdownxModelAdmin


class CommentInline(admin.StackedInline):
    model = Comment


class PostAdmin(MarkdownxModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'created_on', 'published')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
