from django.contrib import admin
from .models import Post, Comment, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status')
    list_filter = ('status', 'user')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    #prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)