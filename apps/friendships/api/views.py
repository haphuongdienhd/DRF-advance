from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.core.pagination import PageNumberPagination

from apps.friendships.exceptions import *
from apps.friendships.api import *
from apps.friendships.models import *

class FriendShipListAPIView(generics.ListAPIView):
    pass

class MyFriendShipListAPIView(generics.ListCreateAPIView):
    pass

class FriendShipRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    pass

class RequestToMeListAPIView(generics.ListAPIView):
    pass

class NewRequestToMeListAPIView(generics.ListAPIView):
    pass

class MyRequestListAPIView(generics.ListAPIView):
    pass

class RequestRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    pass