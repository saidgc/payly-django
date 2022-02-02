from django.db import models
from django.contrib.auth.models import AbstractUser


class PaylyUser(AbstractUser):
    firebase_user_id = models.CharField(max_length=128)
    is_collaborator = models.BooleanField(default=False)
