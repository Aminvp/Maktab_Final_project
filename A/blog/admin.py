from django.contrib import admin
from .models import Post, Comment, Category, Tag


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'body', 'created', 'updated', 'status')
#     prepopulated_fields = {'slug': ('title',)}

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'status')
#     list_filter = ('status', 'user')
#     list_editable = ('status',)
#     search_fields = ('title', 'body')
#     #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)