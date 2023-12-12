from apps.core.exceptions import GenericException


class TokenExpiredException(GenericException):
    code = 8000
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Token is invalid or expired."
        super().__init__(message=message)


class EmailAlreadyVerifiedException(GenericException):
    code = 8001
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "This account has already been verified."
        super().__init__(message=message)


class EmailNotExistException(GenericException):
    code = 8002
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "There is not user exist with this email."
        super().__init__(message=message)


class LinkExpiredException(GenericException):
    code = 8003
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "The link you follow has expired."
        super().__init__(message=message)


class RequireLoginAgainException(GenericException):
    code = 8004
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "You need to login again after changing your password."
        super().__init__(message=message)


class RequireAgreedTermsException(GenericException):
    code = 8006
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "You need to agree with our terms before doing next action."
        super().__init__(message=message)


class OtpInvalidException(GenericException):
    code = 8007
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "The OTP code is invalid."
        super().__init__(message=message)


class OtpExpiredException(GenericException):
    code = 8008
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Your password reset code has expired."
        super().__init__(message=message)


class ChangeSamePasswordException(GenericException):
    code = 8009
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "The new password is the same as the old one."
        super().__init__(message=message)


class PasswordIncorrectException(GenericException):
    code = 8010
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Your password is incorrect."
        super().__init__(message=message)
