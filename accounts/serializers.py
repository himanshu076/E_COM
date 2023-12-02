from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import UserProfile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    # profile_pic_url = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = [
            "age",
            "profile_pic",
            "address",
            "city",
            "state",
            "country",
            "pin_code",
            "occupation",
            "bio",
            "company",
            "website",
            "social_media",
            "updated",
        ]
        read_only_fields = ["user", "updated"]

    # def get_profile_pic_url(self, user_profile):
    #     request = self.context.get('request')
    #     profile_url = user_profile.profile_pic.url
    #     return request.build_absolute_uri(profile_url)


class UserUpdateSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "country_code",
            "phone_number",
            "gender",
            "user_profile",
        ]
        read_only_fields = ["username", "email"]

    def update(self, instance, validated_data):
        if validated_data["country_code"] is None:
            raise serializers.ValidationError(
                _("You should select the country code also.")
            )
        elif validated_data["phone_number"] is None:
            raise serializers.ValidationError(_("You should select the phone number."))
        else:
            # User Data updating here.
            instance.first_name = validated_data.get("first_name", instance.first_name)
            instance.last_name = validated_data.get("last_name", instance.last_name)
            instance.country_code = validated_data.get(
                "country_code", instance.country_code
            )
            instance.phone_number = validated_data.get(
                "phone_number", instance.phone_number
            )
            instance.gender = validated_data.get("gender", instance.gender)

            # Get the nested UserProfile data from validated_data
            user_profile_data = validated_data.get("user_profile")

            # Update the nested UserProfile using UserProfileSerializer's update() method
            if user_profile_data:
                profile_pic = user_profile_data.get("profile_pic", None)
                if profile_pic is None:
                    user_profile_data["profile_pic"] = instance.user_profile.profile_pic
                user_profile_serializer = UserProfileSerializer(
                    instance.user_profile, data=user_profile_data, partial=True
                )
                user_profile_serializer.is_valid(raise_exception=True)
                user_profile_serializer.save()

            instance.save()
            return instance


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["user_profile"]

    def create(self, validated_data):
        if validated_data["password"] != validated_data["confirm_password"]:
            raise serializers.ValidationError(
                _("The two password fields didn't match.")
            )
        else:
            _password = validated_data["password"]

        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            country_code=validated_data["country_code"],
            phone_number=validated_data["phone_number"],
            gender=validated_data["gender"],
            password=_password,
        )
        # user_profile = UserProfile.objects.create(user=user, **user_profile_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password")
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled")
        else:
            raise serializers.ValidationError("Username and password are required")

        attrs["user"] = user
        # return attrs
        return super().validate(attrs)

    def create(self, validated_data):
        user = validated_data["user"]
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        return {"refresh": refresh_token, "access": access_token}


class UserLogoutSerializer(serializers.Serializer):
    pass


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    # user_id = serializers.IntegerField()
    # token = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(min_length=8, write_only=True)

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        # data['user'] = user
        return data

    def save(self, **kwargs):
        user = self.validated_data["user"]
        password = self.validated_data["password"]

        user.set_password(password)
        user.save()
