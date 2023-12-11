import datetime
import json
import logging
import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from model_utils.fields import AutoLastModifiedField
from model_utils.models import SoftDeletableModel, TimeStampedModel

# Create your models here.
class User(AbstractUser, SoftDeletableModel):
    
    USERNAME_FIELD = "username"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modified = AutoLastModifiedField(_("modified"))
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address1 = models.CharField(default="", blank=True, max_length=1000)
    address2 = models.CharField(default="", blank=True, max_length=1000)
    discription = models.CharField(default="", blank=True, max_length=1000)
    display_name = models.CharField(default="", blank=True, max_length=100)
    is_verified = models.BooleanField(
        _("Verified"),
        default=False,
        help_text=_("Designates whether the user have email verified."),
    )
    is_disable = models.BooleanField(default=False, verbose_name="Is disabled")
    is_banned = models.BooleanField(default=False)
    is_banned_by_admin = models.BooleanField(
        default=False, help_text="Will banned all devices and users relevant to this device user if this field marked."
    )
    follower_total = models.PositiveIntegerField(default=0)
    following_total = models.PositiveIntegerField(default=0)
    referring_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="referred_users"
    )
    
    @property
    def name(self):
        name = "%s %s" % (self.first_name, self.last_name)
        if not name.strip():
            name = self.username
        return name
    
    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        if not self.pk and not self.username:
            from allauth.utils import generate_unique_username

            self.username = generate_unique_username(
                [self.first_name, self.last_name, self.email, self.username, "user"]
            )
        self.username = self.username.lower()
        self.first_name = " ".join(self.first_name.split())
        self.last_name = " ".join(self.last_name.split())
        return super().save(*args, **kwargs)
    
    referring_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="referred_users"
    )