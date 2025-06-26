from sqlmodel import SQLModel, Field
import datetime


class PersonSkillHistory(SQLModel, table=True):
    """
    SQLModel PersonSkillHistory
    Purpose: This is a history of skill scores for a person and a skill
    """
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    personskill_id: int | None = Field(default=None, primary_key=True)
    date: datetime.date
    person_id: int = Field(foreign_key="person.person_id")
    skill_id: int = Field(foreign_key="skill.skill_id")
    score: int
