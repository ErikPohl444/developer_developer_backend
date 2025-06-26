import datetime
from sqlmodel import SQLModel, Field


class PersonSkillHistory(SQLModel, table=True):
    personskill_id: int | None = Field(default=None, primary_key=True)
    date: datetime.date
    person_id: int = Field(foreign_key="person.person_id")
    skill_id: int = Field(foreign_key="skill.skill_id")
    score: int
