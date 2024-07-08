from pydantic import BaseModel, UUID4, Field, EmailStr


class UsersInput(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr = Field()
    password: str = Field(min_length=1, max_length=120)

    class Config:
        orm_mode = True


class UsersOutput(BaseModel):
    id: UUID4
    name: str
    email: str

    class Config:
        orm_mode = True

    def verify_password(self, password):
        pass


class AuthenticateUserInput(BaseModel):
    email: EmailStr = Field()
    password: str = Field(min_length=1, max_length=120)


class AuthenticateUserOutput(BaseModel):
    id: UUID4
    name: str
    email: str

