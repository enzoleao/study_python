from fastapi import HTTPException
from app.repositories.users_repository import UsersRepository
from sqlalchemy.orm import Session
from app.schemas.users_schema import UsersInput, UsersOutput, AuthenticateUserOutput, AuthenticateUserInput


class UsersService:
    def __init__(self, session: Session):
        self.repository = UsersRepository(session)

    def authenticate_user(self, data: AuthenticateUserInput) -> AuthenticateUserOutput:
        user = self.repository.find_user_by_email(data.email)

        if not user:
            raise HTTPException(status_code=404, detail="Email or password incorrect")
        print(user.verify_password(data.password))
        # Chama o método verify_password do objeto Users
        if not user.verify_password(data.password):
            raise HTTPException(status_code=400, detail="Email or password incorrect")

        return AuthenticateUserOutput(
            id=user.id,
            name=user.name,
            email=user.email
        )
    def create_user(self, data: UsersInput) -> UsersOutput:
        if self.repository.find_user_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        users = self.repository.create_user(data)
        return UsersOutput(**users.dict(exclude_none=True))
