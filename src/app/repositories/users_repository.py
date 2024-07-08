from sqlalchemy.orm import Session
from app.schemas.users_schema import UsersInput, UsersOutput
from app.models.users import Users


class UsersRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, data: UsersInput) -> UsersOutput:
        users = Users(**data.dict(exclude_none=True))
        self.session.add(users)
        self.session.commit()
        self.session.refresh(users)
        print(users)
        return UsersOutput(id=users.id, name=users.name, email=users.email)

    def find_user_by_email(self, email: str) -> UsersOutput:
        user = self.session.query(Users).filter_by(email=email).first()
        return user
