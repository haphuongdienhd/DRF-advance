from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.rating.models import Rating

class RatingSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Rating
        fields = (
            'blog',
            'reviewer',
            'rating',
            'review',
        )