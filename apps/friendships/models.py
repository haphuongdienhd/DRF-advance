import uuid

from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel

from apps.friendships import choices

# Create your models here.

class FriendshipManager(models.Manager):pass


class Friendship(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendships1")
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendships2")
    is_active = models.BooleanField(default=True)
    
    objects = FriendshipManager()
    
    
class FriendRequestManager(models.Manager):pass


class FriendRequest(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friend_request_from"
    )
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friend_request_to")
    status = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=choices.FRIEND_REQUEST_STATUS_CHOICES,
        default=choices.PENDING,
    )
    viewed = models.DateTimeField(null=True, blank=True)
    
    
    
    objects = FriendRequestManager()