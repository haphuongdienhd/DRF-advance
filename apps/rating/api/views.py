from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.core.pagination import PageNumberPagination

from apps.rating.exceptions import RatingNotFoundException
from apps.rating.api import serializers
from apps.rating.models import Rating
# Create your views here.

class RatingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.RatingSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return Rating.objects.all().order_by('modified')
    
class RatingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RatingSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        try:
            return Rating.objects.get(id=self.kwargs.get("rating_id"))
        except Rating.DoesNotExist:
            raise RatingNotFoundException()
        
    