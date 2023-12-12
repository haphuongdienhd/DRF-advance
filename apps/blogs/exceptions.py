from apps.core.exceptions import GenericException

class BlogNotFoundException(GenericException):
    code = 3000
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Blog not found"
        super().__init__(message=message)
        
class BlogIsPrivateException(GenericException):
    code = 3001
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Blog is private"
        super().__init__(message=message)