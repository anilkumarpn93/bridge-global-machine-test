from django.db import models
from django.utils import timezone
from .user import User


class Deposit(models.Model):
    class Status(models.TextChoices):
        SUCCESS = 'success'
        FAILED = 'failed'

    deposited_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, to_field="customer_xid")
    status = models.CharField(max_length=50, null=False, choices=Status.choices, default=Status.SUCCESS)
    deposited_at = models.DateTimeField(max_length=200, null=True, default=timezone.now())
    amount = models.CharField(max_length=200, default=0, null=False)
    reference_id = models.CharField(max_length=200, default=0, null=False, unique=True)




