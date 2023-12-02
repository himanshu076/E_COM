from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class UsernameOrEmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if username is None:
                username = kwargs.get(User.get_username)

            users = User.objects.filter(
                Q(email__icontains=username) | Q(username__icontains=username)
            )

            # Test whether any matched user has the provided password:
            for user in users:
                if user.check_password(password):
                    return user

            # Verify the password
            if user.check_password(password):
                return user

            raise AuthenticationFailed("Invalid username/email or password.")

        except User.DoesNotExist:
            raise AuthenticationFailed("Invalid username/email or password.")
