from apps.core.exceptions import GenericException

class RatingNotFoundException(GenericException):
    code = 4000
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Rating not found"
        super().__init__(message=message)