from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.blogs.exceptions import NotOwnerException
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
    
    user = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'user',
            'description',
            'categories',
            'content',
            'display_type',
            'is_banned',
        )
        read_only_fields = (
            'is_banned',
        )
        
    def get_user(self, obj):
        return UserSerializer(obj.user).data
    
    def get_categories(self, obj):
        return CategorySerializer(obj.categories, many=True).data
        
    def create(self, validated_data):
        validated_data.update({"user_id": self.context["user_id"],},)
        
        if validated_data.get("categories"):
            validated_data.update({"categories": self.context["categories"],},)
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if instance.user_id != self.context["user_id"]:
            raise NotOwnerException()
        if self.context.get("categories"):
            validated_data.update({"categories": self.context["categories"],},)
        
        return super().update(instance, validated_data)