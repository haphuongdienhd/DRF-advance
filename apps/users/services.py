
from typing import Dict
from allauth.account.models import EmailAddress, EmailConfirmation

from apps.users.exceptions import EmailChangeException, UserNotExistsException
from apps.users.models import User

def get_user(user_id: str) -> User:
    try:
        return User.objects.get(pk=user_id)
    except Exception:
        raise UserNotExistsException()
    

def update_user(instance: User, data: Dict, avatar: str):
    if "email" in data and data.get("email") and data.get("email") != instance.email:
        if not instance.email:
            # Only allow change email here when user don't have email
            raise EmailChangeException()
        instance.email = data.get("email", instance.email)
    instance.first_name = data.get("first_name", instance.first_name)
    instance.username = data.get("username", instance.username)
    instance.last_name = data.get("last_name", instance.last_name)
    instance.date_of_birth = data.get("date_of_birth", instance.date_of_birth)
    instance.address1 = data.get("address1", instance.address1)
    instance.address2 = data.get("address2", instance.address2)
    instance.display_name = data.get("display_name", instance.display_name)
    instance.discription = data.get("discription", instance.bio)
    
    instance.save()
    # if data.get("first_name") != instance.first_name or data.get("last_name") != instance.last_name:
    #     user_updated_display_name_signal.send(sender=User, user=instance)
    return instance


# def archive_report(user: User):
#     ReportUser.objects.filter(to_user=user).update(archived=True)

def update_email_address(instance: User, email):
    email_address = EmailAddress.objects.filter(user=instance).first()
    if not email_address:
        EmailAddress.objects.create(user=instance, email=email, primary=True)
    elif email != email_address.email:
        email_address.email = email
        email_address.verified = False
        email_address.save()
        # resend_confirmation_email(email)
    else:
        return
    instance.is_verified = False