from django.shortcuts import get_object_or_404, render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.core.pagination import PageNumberPagination

from apps.users.api.serializers import UserSerializer
from apps.users.models import User

from apps.friendships.models import Friendship, FriendRequest
from apps.friendships.api.serializers import FriendshipSerializer, FriendRequestSerializer
from apps.friendships.exceptions import FriendshipNotFoundException, MissingToUserIdFieldException, NotYourFriendshipException

class FriendListAPIView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return Friendship.objects.friends_of_user(self.request.user)


class FriendShipRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendshipSerializer
    
    def get_object(self):
        try:
            return Friendship.objects.get(id=self.kwargs.get("friendship_id"))
        except Friendship.DoesNotExist:
            raise FriendshipNotFoundException()
    
    def delete(self, request, *args, **kwargs):
        if self.request.user not in [self.get_object().user1, self.get_object().user2]:
            raise NotYourFriendshipException()
        return super().delete(request, *args, **kwargs)

class RequestToMeListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendRequestSerializer
    
    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user)
    
class NewRequestToMeListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendRequestSerializer
    
    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user,viewed=None)

class MyRequestListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendRequestSerializer
    
    def get_queryset(self):
        return FriendRequest.objects.filter(from_user=self.request.user,viewed=None)
    
    def post(self, request, *args, **kwargs):
        if not self.request.data.get("to_user_id"):
            raise MissingToUserIdFieldException()
        to_user = get_object_or_404(User, id=self.request.data.get("to_user_id"))
        from_user = self.request.user
        return FriendRequest.objects.send(from_user=from_user, to_user__id=to_user)
        

class RequestActionAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FriendRequestSerializer
    
    #TODO action accept/decline request
    #Hint: when accept -> Friendship.make_friend
    #      when decline -> Request.status = DECLINE