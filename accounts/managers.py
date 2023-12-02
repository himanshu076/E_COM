from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from utils.util import randomString


class UserManager(BaseUserManager):
    use_in_migrations = False

    def _create_user(
        self,
        first_name,
        last_name,
        password,
        is_staff,
        is_superuser,
        username=None,
        email=None,
        phone_number=None,
        **kwargs
    ):
        """
        CustomUser Manager for loging vai email or phone.
        """
        now = timezone.now()

        if not first_name:
            raise ValueError("You must enter a first name")

        if not last_name:
            raise ValueError("You must enter a last name")

        if not password:
            raise ValueError("You must enter a password")

        if username is None:
            raise ValueError("You must enter a username")

        if email is None:
            raise ValueError("You must enter a unique email")

        print("Your username is ", username)

        email = self.normalize_email(email)

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            email=email,
            phone_number=phone_number,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    # Creates a normal user
    def create_user(
        self,
        first_name,
        last_name,
        username=None,
        email=None,
        phone_number=None,
        password=None,
        **kwargs
    ):
        return self._create_user(
            first_name,
            last_name,
            password,
            False,
            False,
            username,
            email,
            phone_number,
            **kwargs
        )

    # Creates a superuser
    def create_superuser(
        self,
        first_name,
        last_name,
        username=None,
        email=None,
        phone_number=None,
        password=None,
        **kwargs
    ):
        return self._create_user(
            first_name,
            last_name,
            password,
            True,
            True,
            username,
            email,
            phone_number,
            **kwargs
        )
