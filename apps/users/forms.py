from __future__ import absolute_import, unicode_literals

from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
    UserChangeForm,
    UserCreationForm,
    _unicode_ci_compare,
)

from apps.users.models import User
# from apps.users.services import archive_report

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

    def save(self, commit=True):
        instance = super().save(commit)
        # if "is_banned" in self.changed_data and not instance.is_banned:
        #     archive_report(user=instance)
        return instance


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)
