from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from accounts import views

urlpatterns = [
    # path('user_register/', views.UserRegisterApiView.as_view(), name='user_register'),
    path("user_list/", views.UserListApiView.as_view(), name="user_list"),
    path("user/register/", views.UserRegisterApiView.as_view(), name="user-register"),
    path(
        "user/retrive/<pk>/", views.UserRetrieveApiView.as_view(), name="update_retrive"
    ),
    path("user/update/<pk>/", views.UserUpdateApiView.as_view(), name="update_retrive"),
    # path('retrive_update_profile/<pk>/', views.UserProfileRetrieveUpdateApiView.as_view(), name='retrive_update_profile'),
    path("user/login/", views.UserLoginAPIView.as_view(), name="user-login"),
    path("user/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/logout/", views.UserLogoutAPIView.as_view(), name="user-logout"),
    path(
        "user/password/reset/",
        views.PasswordResetAPIView.as_view(),
        name="password-reset",
    ),
    # path('user/password/reset/confirm/<int:user_id>/<str:token>/', views.PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),
    path(
        "password-reset-confirm/<int:user_id>/<str:token>/",
        views.PasswordResetConfirmAPIView.as_view(),
        name="password-reset-confirm",
    ),
]
