from sqlmodel import SQLModel, Field
import datetime


class Role(SQLModel, table=True):
    """
    SQLModel Role
    Purpose: This is a role which can be held by a person in a team
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    role_id: int | None = Field(default=None, primary_key=True)
    name: str
