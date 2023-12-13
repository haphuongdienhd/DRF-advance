from apps.friendships.models import FriendRequest, Friendship
from django.contrib import admin

from apps.core.admin import StaffAdmin


@admin.register(Friendship)
class FriendshipAdmin(StaffAdmin):
    list_display = ("user1", "user2", "is_active", "created")
    list_filter = ["is_active"]


@admin.register(FriendRequest)
class FriendRequestAdmin(StaffAdmin):
    list_display = ("id", "from_user", "to_user", "status", "viewed", "created", "modified")
    list_filter = ["status"]
