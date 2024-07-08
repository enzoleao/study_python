from app.configs.database import engine
from app.models.users import Users


def create_tables():
    Users.metadata.create_all(bind=engine)
