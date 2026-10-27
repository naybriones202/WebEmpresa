from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_filter = ('published', 'author', 'categories')
    search_fields = ('title', 'content')
    date_hierarchy = 'published'
    filter_horizontal = ('categories',)