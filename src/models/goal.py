from sqlmodel import SQLModel, Field
import datetime


class Goal(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.date
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.date
    goal_id: int | None = Field(default=None, primary_key=True)
    skill_id: int = Field(foreign_key="skill.skill_id")
    name: str
