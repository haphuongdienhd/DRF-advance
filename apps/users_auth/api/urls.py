from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from django.urls import path

from apps.users_auth.api.views import CustomPasswordChange, CustomRegisterView

urlpatterns = [
    path("auth/registration/", CustomRegisterView.as_view(), name="custom_register"),
    path("auth/password/change/", CustomPasswordChange.as_view(), name="rest_password_change"),
]