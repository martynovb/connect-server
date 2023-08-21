from django.db import models
from rest_framework.authtoken.models import Token as DefaultToken
from datetime import timedelta
from django.utils import timezone


class ExpiringToken(DefaultToken):
    expires = models.DateTimeField(default=timezone.now() + timedelta(days=1))
