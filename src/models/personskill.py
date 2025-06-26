from sqlmodel import SQLModel, Field
import datetime


class PersonSkill(SQLModel, table=True):
    """
    SQLModel PersonSkill
    Purpose: This is the current skill level for a person and a skill
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    personskill_id: int | None = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.person_id")
    skill_id: int = Field(foreign_key="skill.skill_id")
    score: int
