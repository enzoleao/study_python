from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = "mysql://root:root@127.0.0.1:9930/backend"

engine = create_engine(CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
        Create a database session.
        Yields:
            Session: The database session.
        """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()