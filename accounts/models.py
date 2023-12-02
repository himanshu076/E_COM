from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager
from utils.constant import Country_Phone_Code, Gender
from utils.util import avatar_upload_location


# Custom User Model Class
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=115)
    last_name = models.CharField(max_length=115)
    username = models.CharField(max_length=115, unique=True)

    email = models.EmailField(blank=False, null=False, unique=True)
    country_code = models.CharField(
        max_length=8, choices=Country_Phone_Code.choices, blank=True, null=True
    )
    phone_number = models.IntegerField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    gender = models.CharField(max_length=5, choices=Gender.choices, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "gender"]
    EMAIL_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        # app_label = "accounts"
        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.email} {self.id}"

    def get_full_name(self):
        if self.first_name != "":
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return {self.username}

    def get_short_name(self):
        return "%s" % (self.first_name)

    # def get_absolute_url(self):
    #     return reverse('user-detail', args=[str(self.id)])

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(
        blank=True, null=True, upload_to=avatar_upload_location
    )
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    pin_code = models.CharField(max_length=10, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=512, blank=True, null=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    social_media = models.URLField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("UserProfile")
        verbose_name_plural = _("UserProfiles")
        # app_label = "accounts"
        ordering = ["-updated"]

    def __str__(self):
        return self.user.email

    # def get_absolute_url(self):
    #     return reverse('user-profile-detail', kwargs={'pk': self.pk})


# class UserAddress(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_address")
#     full_name = models.CharField(max_length=255)
#     mobile = models.IntegerField(blank=True, null=True)
#     address1 = models.CharField(max_length=255)
#     address2 = models.CharField(max_length=255)
#     landmark = models.CharField(max_length=255)
#     pincode = models.CharField(max_length=50, blank=True, null=True)
#     city = models.CharField(max_length=50, null=True, blank=True)
#     state = models.CharField(max_length=50, null=True, blank=True)
#     default = models.BooleanField(default=False)
#     delivery_instructions = models.TextField(max_length=1115)