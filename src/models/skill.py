from sqlmodel import SQLModel, Field
import datetime


class Skill(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.date
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.date
    skill_id: int | None = Field(default=None, primary_key=True)
    name: str
