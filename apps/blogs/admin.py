from django.contrib import admin

from apps.blogs.models import BlogCategory, Category, Blog
from apps.core.admin import StaffAdmin

# Register your models here.
class ProductCategoryInline(admin.TabularInline):    
    model=BlogCategory
    list_per_page = 10
    raw_id_fields=('category',)    

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
        'category',
        'is_private',
        'is_public',
        'is_banned',
    )
    inlines=[ProductCategoryInline]
    list_filter = ["user","categories"]
    
    @admin.display(empty_value="???")
    def category(self, blog):
        procates = BlogCategory.objects.filter(blog=blog)
        categories = ' '
        for cate in procates:
            categories += str(cate.category.name + ', ')
            
        return categories