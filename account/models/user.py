from django.contrib.auth.models import AbstractUser
from django.db import models

MAX_LENGTH = 128


class PaylyUser(AbstractUser):
    firebase_user_id = models.CharField(max_length=MAX_LENGTH)
    is_collaborator = models.BooleanField(default=False)
