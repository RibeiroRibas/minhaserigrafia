from enum import Enum

from app.errors.models.error_model import ErrorModel


class BaseErrorCode(Enum):

    def code(self):
        return self.value[0]

    def message(self):
        return self.value[1]


def __build_doc_description(errors: list[BaseErrorCode]) -> str:
    description: str = ""
    for error in errors:
        if description == "":
            description = f"{error.code()}: {error.message()}"
        else:
            description = f"{description}   |   {error.code()}: {error.message()}"
    return description


def build_doc_errors_response(errors: list[BaseErrorCode]):
    return {
        "description": __build_doc_description(errors),
        "model": ErrorModel
    }
