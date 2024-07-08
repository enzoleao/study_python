from fastapi import APIRouter, Depends
from app.schemas.users_schema import UsersOutput, UsersInput, AuthenticateUserInput,AuthenticateUserOutput
from sqlalchemy.orm import Session
from app.configs.database import get_db
from app.services.users_service import UsersService
router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "resource Not found"}},
)


@router.get("")
def get_users():
    return {"message": "Hello World"}


@router.post("", status_code=201, response_model=UsersOutput)
def create_user(
        data: UsersInput,
        session: Session = Depends(get_db),
):
    _service = UsersService(session)
    return _service.create_user(data)

@router.post("/authenticate",status_code=200, response_model=AuthenticateUserOutput)
def authenticate_user(data: AuthenticateUserInput, session: Session = Depends(get_db)):
    _service = UsersService(session)
    return _service.authenticate_user(data)