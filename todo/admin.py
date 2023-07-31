from django.contrib import admin

from todo import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'category']
    list_per_page = 10
    list_filter = ['category', 'user']
    ordering = ['user', 'completed', 'title']
    search_fields = ['title']
    search_help_text = 'search on titles'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
