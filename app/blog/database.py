from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
"""
Base use for crate   data modules in  database

"""
def get_db():
    """
    here the get_db() used for getting connection of database

    and  close the database connection at  the end..

    """
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    