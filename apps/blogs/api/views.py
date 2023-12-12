from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.core.pagination import PageNumberPagination

from apps.blogs.exceptions import BlogIsPrivateException, BlogNotFoundException
from apps.blogs.api import serializers
from apps.blogs.models import Blog
# Create your views here.

class BlogListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.BlogSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return Blog.objects.filter(is_private=False,is_banned=False).order_by('modified')
    
class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BlogSerializer
    
    def get_object(self):
        try:
            obj = Blog.objects.get(id=self.kwargs.get("blog_id"))
            if self.request.user != obj.user and obj.is_private:
                raise BlogIsPrivateException()
        except Blog.DoesNotExist:
            raise BlogNotFoundException()
        
    