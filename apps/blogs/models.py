import uuid

from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel

from apps.blogs import choices

# Create your models here.

class Category(TimeStampedModel):
    UNCATEGORIZED = "Uncategorized"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @classmethod
    def get_or_create_default_category(cls):
        category, _ = Category.objects.get_or_create(name=Category.UNCATEGORIZED)
        return category


class Blog(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='categories',through='BlogCategory')
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, blank=True, null=True,)
    #rating????????????TODO
    
    display_type = models.CharField(max_length=50, choices=choices.DISPLAY_CHOICES, default=choices.PUBLIC)
    is_banned = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"
    
class BlogCategory(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'blogs_blog_category'