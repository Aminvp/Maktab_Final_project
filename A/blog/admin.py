from django.contrib import admin
from .models import Post, Comment, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status')
    list_filter = ('status', 'user')
    list_editable = ('status',)
    search_fields = ('title', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'is_reply', 'created', 'updated')
    list_filter = ('post', 'user', 'reply')
    list_editable = ('is_reply',)
    search_fields = ('post', 'body')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)