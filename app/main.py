from fastapi import FastAPI

from app.errors.handler.error_handler import add_error_handler
from app.api.v1.router_v1 import router_v1

app = FastAPI()

app.include_router(router_v1, prefix='/api/app')

add_error_handler(app)