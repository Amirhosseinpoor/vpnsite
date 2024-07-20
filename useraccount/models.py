from django.contrib.auth.models import AbstractUser
from django.db import models

month_choice = [
    ('1_month', '1_Month'),
    ('3_month', '3_Month'),
    ('6_month', '6_Month'),
    ('12_month', '12_Month'),
]
user_choice = [
    ('1_user', '1_User'),
    ('2_user', '2_User'),
    ('3_user', '3_User'),
    ('4_user', '4_User'),
    ('unlimited_user', 'Unlimited_user')

]


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    identifier_name = models.CharField(max_length=255, blank=False, default='default_identifier')
    email = models.EmailField(blank=False)
    telegram_id = models.CharField(max_length=255, blank=False, default='default_telegram_id')
    vpn_link = models.TextField(blank=True)
    fragment = models.CharField(max_length=255, blank=True)
    month = models.CharField(max_length=20, blank=True, choices=month_choice, default='1_month')
    user = models.CharField(max_length=20, blank=True, choices=user_choice, default='1_user')

    def __str__(self):
        return self.username
