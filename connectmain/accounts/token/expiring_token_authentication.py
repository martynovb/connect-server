from datetime import timedelta

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone


class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        token, user = super().authenticate_credentials(key)

        if token.expires < timezone.now():
            raise AuthenticationFailed("Token has expired")

        # Update the token's expiration time each time a user makes a request
        token.expires = timezone.now() + timedelta(days=1)
        token.save()

        return token, user
