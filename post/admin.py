from django.contrib import admin
from post.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'created_at']
    list_display_links = ['id', 'title', 'author', 'category']
    list_filter = ['category', 'author']
    search_fields = ['title', 'content']
