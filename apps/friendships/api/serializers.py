from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from apps.friendships.models import Friendship, FriendRequest

from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class FriendshipSerializer(serializers.Serializer):
    
    user1 = serializers.SerializerMethodField()
    user2 = serializers.SerializerMethodField()
    
    class Meta:
        model = Friendship
        field = (
            'id',
            'user1',
            'user2',
        )
        
    def get_user1(self, obj):
        return UserSerializer(obj.user1).data
    
    def get_user2(self, obj):
        return UserSerializer(obj.user2).data
    
class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = serializers.SerializerMethodField()
    to_user = serializers.SerializerMethodField()

    class Meta:
        model = FriendRequest
        fields = [
            "id",
            "from_user",
            "to_user",
            "status",
            "created",
            "modified",
        ]

    def get_from_user(self, obj):
        return UserSerializer(obj.from_user).data

    def get_to_user(self, obj):
        return UserSerializer(obj.to_user).data