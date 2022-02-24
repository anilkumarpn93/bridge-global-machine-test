from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    customer_xid = models.CharField(max_length=200, blank=True, unique=True)
