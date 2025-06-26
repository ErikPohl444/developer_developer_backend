from sqlmodel import SQLModel, Field
import datetime


class Skill(SQLModel, table=True):
    """
    SQLModel Skill
    Purpose: This is a skill used by a team or by a person
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    skill_id: int | None = Field(default=None, primary_key=True)
    name: str
