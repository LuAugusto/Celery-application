class AbstractAPIException(Exception):
    def __init__(self, message: str, code: str, name: str, status_code: int) -> None:
        super().__init__()

        self.code = code
        self.name = name
        self.message = message
        self.status_code = status_code


class RequestError(AbstractAPIException):
    def __init__(self, message="Request error") -> None:
        super().__init__(message, "An error has occurred while to trying request", 'not_found', 400)