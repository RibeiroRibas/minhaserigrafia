from app.errors.base_error import BaseError


class ForbiddenError(BaseError):

    def __init__(self, code: int) -> None:
        super().__init__(code)

    def get_code(self) -> int:
        return self.code
