from fastapi import APIRouter
from app.controllers import (
    users_controller
)

router = APIRouter(
    prefix="/v1",
    responses={404: {"description": "Not found"}},
)

router.include_router(users_controller.router)
