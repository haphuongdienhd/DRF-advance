from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from rest_framework.serializers import ValidationError as DRFValidationError

from apps.users.exceptions import ValidateUserException
from apps.users.models import User
from apps.users.services import (
    update_email_address, 
    update_user,
)
from apps.users.validator import EmailValidator
from apps.users_auth.exceptions import (
    ChangeSamePasswordException,
    PasswordIncorrectException,
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "date_of_birth",
            "address1",
            "address2",
            "discription",
            "display_name",
            "is_verified",
        )
        validators = [UniqueTogetherValidator(queryset=User.objects.all(), fields=["username"])]

    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, validators=[EmailValidator()])

    def validate_first_name(self, first_name):
        if first_name and len(first_name) < 2:
            raise ValidateUserException("First name must be at least 2 characters.")
        return first_name

    def validate_last_name(self, last_name):
        if last_name and len(last_name) < 2:
            raise ValidateUserException("Last name must be at least 2 characters.")
        return last_name

    def update(self, instance: User, validated_data):
        validated_data["display_name"] = self.initial_data.get("display_name", "")

        if "email" in self.validated_data:
            if (
                User.objects.filter(email__iexact=self.validated_data.get("email").lower())
                .exclude(id=instance.id)
                .exists()
            ):
                raise DRFValidationError("A user is already registered with this e-mail address.", code=2004)
        old_email = instance.email
        instance = update_user(instance, validated_data)
        if "email" in self.validated_data and instance.email != old_email:
            update_email_address(instance=instance, email=self.validated_data.get("email").lower())

        if "password" in self.validated_data and not instance.password:
            instance.set_password(self.validated_data["password"])
            instance.save()

        return instance

class UserProfileSerializer(UserSerializer):
    password_exist = serializers.SerializerMethodField()
    # display_name = serializers.SerializerMethodField()
    # is_blocked = serializers.SerializerMethodField()
    # blocked = serializers.SerializerMethodField()
    # personal_url = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    # current_is_follower = serializers.SerializerMethodField()
    # current_is_following = serializers.SerializerMethodField()
    # referring_user = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        model = User
        fields = UserSerializer.Meta.fields + (  # type: ignore
            "password_exist",
            "is_removed",
            # "is_blocked",
            # "blocked",
            "password",
            "confirm_password",
            # "personal_url",
            "follower_total",
            "following_total",
            # "current_is_follower",
            # "current_is_following",
            "referring_user",
        )

        read_only_fields = (
            "follower_total",
            "following_total",
            "referring_user",
        )

    def validate(self, data):
        if "password" in data and data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    # def get_is_blocked(self, obj):
    #     request_user = self.context["user"] if "user" in self.context else None
    #     is_blocked = BlockUser.objects.filter(from_user_id=obj.id, to_user=request_user).exists()
    #     return is_blocked

    # def get_blocked(self, obj):
    #     request_user = self.context["user"] if "user" in self.context else None
    #     blocked = BlockUser.objects.filter(from_user=request_user, to_user_id=obj.id).exists()
    #     return blocked

    # @classmethod
    # def get_is_email_verified(cls, obj):
    #     try:
    #         email_address = EmailAddress.objects.get(user=obj)
    #         return email_address.verified
    #     except EmailAddress.DoesNotExist:
    #         return False

    @classmethod
    def get_password_exist(cls, obj):
        pwd_exist = True
        if not obj.password or obj.password.startswith(UNUSABLE_PASSWORD_PREFIX):
            pwd_exist = False
        return pwd_exist

    # def get_email_temp(self, obj):
    #     email_temp = EmailAddressTemporary.objects.filter(user_id=obj.pk).first()
    #     return EmailAddressTemporarySerializer(instance=email_temp).data if email_temp else None

    # def get_current_is_follower(self, obj):
    #     # TODO: optimize N+1
    #     request_user = self.context["user"] if self.context.get("user") else self.context.get("request").user
    #     return obj.followers.filter(followed_by=request_user, is_active=True).exists()

    # def get_current_is_following(self, obj):
    #     # TODO: optimize N+1
    #     request_user = self.context["user"] if self.context.get("user") else self.context.get("request").user
    #     return obj.following.filter(user=request_user, is_active=True).exists()

    # def get_referring_user(self, obj):
    #     return LightweightUserSerializer(instance=obj.referring_user).data if obj.referring_user else None
    
class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, required=True)
    new_password1 = serializers.CharField(
        max_length=128,
        allow_blank=True,
    )
    new_password2 = serializers.CharField(max_length=128, allow_blank=True)

    def validate(self, attrs):
        old_pwd = attrs.get("old_password")
        new_pwd1 = attrs.get("new_password1")
        new_pwd2 = attrs.get("new_password2")
        user = self.context["user"]
        if not user.check_password(old_pwd):
            raise PasswordIncorrectException
        if any([old_pwd == new_pwd1, old_pwd == new_pwd2]):
            raise ChangeSamePasswordException
        return attrs

    def save(self):
        user = self.context["user"]
        user.set_password(self.validated_data["new_password1"])
        user.save()
        return user