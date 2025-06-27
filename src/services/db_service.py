from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine
from fastapi import Depends

sqlite_file_name = "./data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def connect_to_db():  # stub, inspiration
    pass  # place holder


def get_db():  # stub, inspiration
    db = connect_to_db()
    try:
        yield db
    finally:
        db.close()
