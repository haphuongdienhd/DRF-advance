import uuid

from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel

from apps.blogs.models import Blog

from apps.rating.choices import RATE_CHOICES

# Create your models here.

class Rating(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_reviewed")
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviewer")
    rating = models.SmallIntegerField(choices=RATE_CHOICES, null=True, blank=True)
    review = models.TextField(null=True, blank=True, default="")
