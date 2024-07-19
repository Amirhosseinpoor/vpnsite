from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    identifier_name = models.CharField(max_length=255, blank=False, default='default_identifier')
    email = models.EmailField(blank=False)
    telegram_id = models.CharField(max_length=255, blank=False, default='default_telegram_id')

    def __str__(self):
        return self.username
