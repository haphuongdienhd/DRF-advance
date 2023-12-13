from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from apps.rating.exceptions import NotOwnerRatingException, SelfRatingException

from apps.rating.models import Rating

from apps.blogs.models import Blog
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class RatingSerializer(serializers.ModelSerializer):
    
    reviewer = serializers.SerializerMethodField()
    
    class Meta:
        model = Rating
        fields = (
            'blog',
            'reviewer',
            'rating',
            'review',
        )
        
    def get_reviewer(self, obj):
        return UserSerializer(obj.reviewer).data
    
    def create(self, validated_data):
        validated_data.update(
            {"reviewer_id": self.context["reviewer_id"]},
        )
        if validated_data['blog'].user.id == self.context["reviewer_id"]:
            raise SelfRatingException()
        instance = Rating.objects.filter(blog=validated_data['blog'],reviewer_id=self.context["reviewer_id"]).first()
        if instance:
            return self.update(instance, validated_data)
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if instance.reviewer_id != self.context["reviewer_id"]:
            raise NotOwnerRatingException()
        return super().update(instance, validated_data)