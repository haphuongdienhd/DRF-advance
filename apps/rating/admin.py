from django.contrib import admin
from apps.core.admin import StaffAdmin

from apps.rating.models import Rating

# Register your models here.

@admin.register(Rating)
class CategoryAdmin(StaffAdmin):
    list_display = (
        "blog",
        "reviewer",
        "rating",
        "review",
    )
    search_fields = ("blog",)