"""
URL configuration for online_marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenVerifyView

# from dj_rest_auth.registration.views import (RegisterView, VerifyEmailView,
#                                             ConfirmEmailView ,ResendEmailVerificationView)
# from dj_rest_auth.views import (LoginView, LogoutView, UserDetailsView,
#                             PasswordResetConfirmView, PasswordResetView)


schema_view = get_schema_view(
    openapi.Info(
        title="Online Marketplace API",
        default_version="v1",
        description="buy & selling product",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  # Set it to False if you want to require authentication
    permission_classes=(
        permissions.AllowAny,
    ),  # Set it to [JWTAuthentication] for JWT authentication
    authentication_classes=[
        JWTAuthentication
    ],  # Set it to [JWTAuthentication] for JWT authentication
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("cotegories.urls")),
    path("products/", include("products.urls")),
    path("", include("payment.urls")),
    path("", include("order_management.urls")),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    
    # JWT urls
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]

# urlpatterns += [
#     # path('admin/', admin.site.urls),
#     # path('accounts/', include('accounts.urls')),
#     # path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),

#     # path("register/", RegisterView.as_view(), name="rest_register"),
#     path("login/", LoginView.as_view(), name="rest_login"),
#     path("logout/", LogoutView.as_view(), name="rest_logout"),
#     path("user/", UserDetailsView.as_view(), name="rest_user_details"),

#     # This url verify the email.
#     # path("register/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
#     # # This URL is used to send verification mail on user email.
#     # path("account-confirm-email/", VerifyEmailView.as_view(), name="account_email_verification_sent"),
#     # # This url Confirm the email.
#     # path("account-confirm-email/<str:key>/", VerifyEmailView.as_view(), name="account_confirm_email"),
#     # # This url Resend the email verification link to user email again.
#     # path("register/resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"),
#     # This url is use to reset the password of logined user.
#     path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),

#     path("password/reset/confirm/<str:uidb64>/<str:token>/", PasswordResetView.as_view(), name="password_reset_confirm",),
#     path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
# ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
