from apps.core.exceptions import GenericException

class SelfActionException(GenericException):
    code = 5000
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "The user is trying to perform an action over itself"
        super().__init__(message=message)
        
class FriendshipNotFoundException(GenericException):
    code = 5001
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Friendship not found"
        super().__init__(message=message)
        
class NotYourFriendshipException(GenericException):
    code = 5002
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Not your friendship"
        super().__init__(message=message)
        
class AlreadyFriendException(GenericException):
    code = 5003
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Two users are already friends"
        super().__init__(message=message)
        
class ActionNotException(GenericException):
    code = 5004
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Two users are already friends"
        super().__init__(message=message)
        
class AlreadySendRequestException(GenericException):
    code = 5005
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Already send request"
        super().__init__(message=message)
        
class MissingToUserIdFieldException(GenericException):
    code = 5006
    verbose = True

    def __init__(self, message=None):
        if not message:
            message = "Missing to_user_id field"
        super().__init__(message=message)