from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = getenv("DATABASE_URL")
try:
    engine = create_engine(str(DATABASE_URL))
except:
    print("No database URL found, db operations not available.")
    pass


def get_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()