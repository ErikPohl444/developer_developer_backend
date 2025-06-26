from sqlmodel import SQLModel, Field
import datetime


class PersonGoal(SQLModel, table=True):
    """
    SQLModel PersonGoal
    Purpose: Set targets for a person for a skill with a due date
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    persongoal_id: int | None = Field(default=None, primary_key=True)
    skill_id: int = Field(foreign_key="skill.skill_id")
    person_id: int = Field(foreign_key="person.person_id")
    exceeds_score: int
    due_date: datetime.date
