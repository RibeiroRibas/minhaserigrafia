from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.errors.bad_request_error import BadRequestError
from app.errors.models.error_model import ErrorModel
from app.errors.forbidden_error import ForbiddenError
from app.errors.internal_error import InternalError
from app.errors.not_found_error import NotFoundError
from app.errors.unauthorized_error import UnauthorizedError


def add_error_handler(app: FastAPI):
    @app.exception_handler(UnauthorizedError)
    async def unauthorized_error_handler(_, exc: UnauthorizedError):
        return JSONResponse(
            status_code=401,
            content=ErrorModel(code=exc.code).model_dump()
        )

    @app.exception_handler(InternalError)
    async def internal_error_handler(_, exc: InternalError):
        return JSONResponse(
            status_code=500,
            content=ErrorModel(code=exc.code).model_dump()
        )

    @app.exception_handler(NotFoundError)
    async def not_found_error_handler(_, exc: NotFoundError):
        return JSONResponse(
            status_code=404,
            content=ErrorModel(code=exc.code).model_dump()
        )

    @app.exception_handler(BadRequestError)
    async def bad_request_error_handler(_, exc: BadRequestError):
        return JSONResponse(
            status_code=400,
            content=ErrorModel(code=exc.code).model_dump()
        )

    @app.exception_handler(ForbiddenError)
    async def bad_request_error_handler(_, exc: BadRequestError):
        return JSONResponse(
            status_code=400,
            content=ErrorModel(code=exc.code).model_dump()
        )
