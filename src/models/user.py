from sqlmodel import SQLModel, Field
import datetime


class User(SQLModel, table=True):
    """
    SQLModel User
    Purpose: A user uses the system to define teams, set individual and team goals, and track progress
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    user_id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str
    pwd: str
