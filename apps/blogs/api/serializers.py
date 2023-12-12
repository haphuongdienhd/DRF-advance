from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.blogs.models import Blog, Category
from apps.users.api.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
        
        
class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = (
            'title',
            'user',
            'description',
            'categories',
            'content',
            'is_private',
            'is_public',
            'is_banned',
        )
        read_only_fields = (
            'is_banned',
        )