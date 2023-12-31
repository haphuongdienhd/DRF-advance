from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.core.pagination import PageNumberPagination

from apps.blogs import choices
from apps.blogs.exceptions import BlogIsPrivateException, BlogNotFoundException, NotOwnerException
from apps.blogs.api import serializers
from apps.blogs.models import Blog
# Create your views here.

class BlogListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.BlogSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        where = Q(display_type=choices.PUBLIC)
        return Blog.objects.filter(where, is_banned=False).order_by('modified')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(user_id=self.request.user.id)
        if self.request.data.get("categories"):
            context.update(categories=self.request.data.get("categories"))
        return context
        
    
class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BlogSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        try:
            obj = Blog.objects.get(id=self.kwargs.get("blog_id"))
            if self.request.user != obj.user and obj.is_private:
                raise BlogIsPrivateException()
            return obj
        except Blog.DoesNotExist:
            raise BlogNotFoundException()
        
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(user_id=self.request.user.id)
        if self.request.data.get("categories"):
            context.update(categories=self.request.data.get("categories"))
        return context
    
    def delete(self, request, *args, **kwargs):
        if self.get_object().user != self.request.user:
            raise NotOwnerException()
        return super().delete(request, *args, **kwargs)