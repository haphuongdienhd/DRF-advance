from apps.core.exceptions import GenericException


class MissedUsernameOrEmailException(GenericException):
    code = 2000
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Username or email is required."
        super().__init__(message=message)


class EmailToResetNotExistException(GenericException):
    code = 2001
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "This e-mail address does not exist."
        super().__init__(message=message)


class EmailRegisteredNotVerifiedException(GenericException):
    code = 2002
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "This e-mail address is not verified. Please check your mailbox."
        super().__init__(message=message)


class PasswordsNotMatchException(GenericException):
    code = 2003
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "The two password fields didn't match."
        super().__init__(message=message)


class UsernameRegisteredWithThisEmailException(GenericException):
    code = 2004
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "A user is already registered with this e-mail address."
        super().__init__(message=message)


class UsernameAlreadyExistException(GenericException):
    code = 2005
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Username is already existed."
        super().__init__(message=message)


class PasswordValidateError(GenericException):
    code = 2006
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Password is not valid. Please try again."
        super().__init__(message=message)


class EmailValidateError(GenericException):
    code = 2007
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Email is not valid. Please try again."
        super().__init__(message=message)


class UserAccountDisabledException(GenericException):
    code = 2008
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "User account is disabled."
        super().__init__(message=message)


class LogInException(GenericException):
    code = 2009
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Your credential is incorrect."
        super().__init__(message=message)


class PasswordException(GenericException):
    code = 2010
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Please enter the current password correctly"
        super().__init__(message=message)


class PasswordResetOTPException(GenericException):
    code = 2011
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Unable to reset password."
        super().__init__(message=message)


class UserNotExistsException(GenericException):
    code = 2016
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "User does not exist"
        super().__init__(message=message)


class UserIsDisableException(GenericException):
    code = 2017
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "This user account is not available."
        super().__init__(message=message)


class UserIsDisabledByReportException(GenericException):
    code = 2018
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = (
                "This user account is disabled because we received number per of reports about your account "
                "has not pass Terms and Conditions "
            )
        super().__init__(message=message)


class UserIsNotProviderException(GenericException):
    code = 2019
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "User is not provider or the account is not approved."
        super().__init__(message=message)


class UserIsNotPatientException(GenericException):
    code = 2020
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "User is not patient."
        super().__init__(message=message)


class CheckPasswordException(GenericException):
    code = 2021
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "The old password and the new password must be different."
        super().__init__(message=message)


class ValidateUserException(GenericException):
    code = 2022
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "User must be at least 18 years old."
        super().__init__(message=message)


class SendEmailException(GenericException):
    code = 2023
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Mail has been sent, please try again in a minute."
        super().__init__(message=message)


class InvalidPasswordException(GenericException):
    code = 2024
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Your password is incorrect."
        super().__init__(message=message)


class EmailChangeException(GenericException):
    code = 2025
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "please use change email function if you want to set new email."
        super().__init__(message=message)


class UserPermissionException(GenericException):
    code = 2031
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Sorry, You have no permission to do this action."
        super().__init__(message=message)


class EmailIsExistedException(GenericException):
    code = 2032
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "The email address you entered is already registered. Please try another email address."
        super().__init__(message=message)


class UserBlockedException(GenericException):
    code = 2034
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Sorry, You can not process this action."
        super().__init__(message=message)


class UserAccountIsBannedByAdminException(GenericException):
    code = 2037
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "This user has been banned by admin. Please contact to admin to have more support."
        super().__init__(message=message)


class AccountDeletionRequestNotValid(GenericException):
    code = 2048
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Your account deletion request is invalid. Try again with correct information!"
        super().__init__(message=message)
