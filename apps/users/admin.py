from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User
from apps.users.forms import CustomUserChangeForm, CustomUserCreationForm

from apps.core.admin import StaffAdmin

# Register your models here.
class UserAdmin(AuthUserAdmin, StaffAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "is_verified",
                    "is_banned",
                    "is_banned_by_admin",
                    "active_secret_questions",
                    "profile_complete",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                    "date_of_birth",
                    "address1",
                    "address2",
                    "city",
                    "state",
                    "zip_code",
                    "stripe_customer_id",
                    "device_id",
                    "password_change_count",
                    "agreed_terms",
                    "follower_total",
                    "following_total",
                    "enabled_2fa",
                    "enabled_2fa_email",
                    "enabled_2fa_phone",
                    "referring_user",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                )
            },
        ),
        (
            _("Meta Data"),
            {"fields": ("metadata", "last_transaction")},
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "modified",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "username",
        "follower_total",
        "following_total",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_verified",
        "is_banned",
        "is_banned_by_admin",
        "date_joined",
        "modified",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-date_joined",)
    list_filter = ("is_active", "is_verified", "is_banned")

    readonly_fields = AuthUserAdmin.readonly_fields + (
        "last_login",
        "date_joined",
    )
    raw_id_fields = ["referring_user"]

    def get_fieldsets(self, request, obj=None):
        if obj:
            fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
            if not request.user.is_superuser:
                # Remove permission module for staff users
                fieldsets = fieldsets[:2] + fieldsets[3:]
            return fieldsets
        else:
            return self.add_fieldsets

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.is_verified:
            return self.readonly_fields + ("is_verified",)
        return self.readonly_fields

    def delete_model(self, request, obj):
        User.objects.filter(id=obj.id).delete()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)