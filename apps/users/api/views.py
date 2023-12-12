from django.shortcuts import render

from rest_framework import generics

from apps.users.api import serializers
# Create your views here.

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserProfileSerializer

    def get_object(self):
        return self.request.user