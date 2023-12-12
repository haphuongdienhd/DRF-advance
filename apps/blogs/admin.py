from django.contrib import admin

from apps.blogs.models import Category, Blog
from apps.core.admin import StaffAdmin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(StaffAdmin):
    list_display = (
        "name",
        "created",
        "modified",
    )
    search_fields = ("name",)
    
@admin.register(Blog)
class BlogAdmin(StaffAdmin):
    list_display = (
        'title',
        'user',
        'description',
        'content',
        'is_private',
        'is_public',
        'is_banned',
    )
    filter_horizontal = ('categories',)
    list_filter = ["user","categories"]