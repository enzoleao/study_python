import uuid
from sqlalchemy import Column, String,DateTime
from app.configs.database import Base
import bcrypt
import datetime
class Users(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    _password = Column('password', String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        self._password = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, plaintext_password):
        return bcrypt.checkpw(plaintext_password.encode('utf-8'), self._password.encode('utf-8'))
