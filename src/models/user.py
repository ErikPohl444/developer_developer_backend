from sqlmodel import SQLModel, Field
import datetime


class User(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.date
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.date
    user_id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str
