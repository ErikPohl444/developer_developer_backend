from sqlmodel import SQLModel, Field
import datetime


class Person(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    person_id: int | None = Field(default=None, primary_key=True)
    name: str
    role_id: int = Field(foreign_key="role.role_id")
