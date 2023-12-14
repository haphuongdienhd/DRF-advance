import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import F, Q

from model_utils.models import TimeStampedModel

from apps.friendships import choices
from apps.friendships.exceptions import AlreadyFriendException, AlreadySendRequestException, SelfActionException

# Create your models here.

class FriendshipManager(models.Manager):
    
    def _sort_user_pair(self, user1, user2):
        if user1.id == user2.id:
            raise SelfActionException()
        sorted_user_pair = sorted([user1, user2], key=lambda u: u.id)
        return sorted_user_pair[0], sorted_user_pair[1]
    
    def make_friend(self, user1, user2, **kwargs):
        user1, user2 = self._sort_user_pair(user1, user2)
        if self.be_friends(user1, user2):
            raise AlreadyFriendException()

        where = Q(from_user=user1, to_user=user2) | Q(from_user=user2, to_user=user1)
        FriendRequest.objects.filter(where).delete()

        obj, created = self.update_or_create(user1=user1, user2=user2)
        return obj
    
    def be_friends(self, user1, user2, **kwargs):
        user1, user2 = self._sort_user_pair(user1, user2)
        return self.filter(user1=user1, user2=user2).exists()
    
    def friends_of_user(self, user, **kwargs):
        where = Q(user1=user) | Q(user2=user)
        friendships = Friendship.objects.filter(where).select_related("user1", "user2")
        return [friendship.user1 if user != friendship.user1 else friendship.user2 for friendship in friendships]


class Friendship(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendships1")
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="friendships2")
    
    objects = FriendshipManager()
    
    class Meta:
        indexes = [
            models.Index(fields=["user1", "user2"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["user1", "user2"],
                name="unique_user_pair",
            ),
            models.CheckConstraint(
                name="prevent_self_friend",
                check=~Q(user1=F("user2")),
            ),
        ]
    
    
class FriendRequestManager(models.Manager):
    def send(self, from_user, to_user, **kwargs):
        if from_user.id == to_user.id:
            raise SelfActionException()
        if Friendship.objects.be_friends(user1=from_user, user2=to_user):
            raise AlreadyFriendException()

        friend_request, created = self.get_or_create(from_user=from_user, to_user=to_user)
        if not created and friend_request.status == choices.PENDING:
            raise AlreadySendRequestException()
        if not created:
            friend_request.status = choices.PENDING
            friend_request.save()
        return friend_request

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
    
    def mark_viewed(self):
        self.viewed = timezone.now()
        self.save()
        return True
    
    objects = FriendRequestManager()