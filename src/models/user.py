from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str
