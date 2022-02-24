from django.db import models
from .base import Base
from django.utils import timezone
from .user import User


class Wallet(Base):
    class Status(models.TextChoices):
        ENABLED = 'enabled'
        DISABLED = 'disabled'

    owned_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, to_field="customer_xid", unique=True)
    status = models.CharField(max_length=50, null=False, choices=Status.choices, default=Status.ENABLED)
    enabled_at = models.DateTimeField(max_length=200, null=True, default=timezone.now())
    balance = models.CharField(max_length=200, default=0, null=False)


