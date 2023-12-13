from apps.core.exceptions import GenericException

class RatingNotFoundException(GenericException):
    code = 4000
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Rating not found"
        super().__init__(message=message)
        
class SelfRatingException(GenericException):
    code = 4001
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Self rating is not allowed"
        super().__init__(message=message)
        
class NotOwnerRatingException(GenericException):
    code = 4003
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "You are not rating's owner"
        super().__init__(message=message)