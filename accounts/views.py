# from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User, UserProfile
from accounts.serializers import (PasswordResetConfirmSerializer,
                                  PasswordResetRequestSerializer,
                                  UserLoginSerializer, UserLogoutSerializer,
                                  UserSerializer, UserUpdateSerializer)
from utils.permissions import IsOwner


# Create your views here.
class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserRegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login_data = serializer.save()
        return Response(login_data, status=200)


class UserRetrieveApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    authentication_classes = [JWTAuthentication]


class UserUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    authentication_classes = [JWTAuthentication]


class UserLogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    allowed_methods = ["POST"]
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        if user:
            try:
                refresh = RefreshToken.for_user(user)
                refresh_token = str(refresh)
                if refresh_token:
                    token = RefreshToken(refresh_token)
                    token.blacklist()

                    # Optionally, generate a new access token to provide a seamless logout experience
                    access_token = token.access_token

                    return Response(
                        {
                            "detail": "Successfully logged out.",
                            "access_token": str(access_token),
                        },
                        status=200,
                    )
                else:
                    return Response({"error": "No refresh token found."}, status=400)
            except Exception:
                return Response({"error": "Invalid refresh token."}, status=400)

        return Response({"error": "User not found."}, status=400)


class PasswordResetAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data["email"])
        # email = request.data.get('email')
        # user = get_object_or_404(User, email=email)
        token = default_token_generator.make_token(user)
        reset_link = f"{settings.FRONTEND_URL}/password-reset-confirm/{user.id}/{token}"
        send_mail(
            "Password Reset",
            f"Click the link below to reset your password:\n{reset_link}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return Response(
            {"detail": "Password reset link has been sent to your email."},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_fields = ("user_id", "token")

    def get_object(self):
        user_id = self.kwargs.get("user_id")
        token = self.kwargs.get("token")
        user = get_object_or_404(User, id=user_id)
        if not default_token_generator.check_token(user, token):
            raise Http404
        return user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        password = request.data.get("password")
        user.set_password(password)
        user.save()
        return Response(
            {"success": "Password reset successfully"}, status=status.HTTP_200_OK
        )


# class UserProfileRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     # permission_classes = [IsAuthenticated]
