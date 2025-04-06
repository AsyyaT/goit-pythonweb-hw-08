from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.conf.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata_ = MetaData()


class Base(DeclarativeBase):
    __abstract__ = True
    metadata = metadata_


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
