from django.db import models
from django.utils import timezone
from api.models.user import User


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        ordering = ['created_at']

