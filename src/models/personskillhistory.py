import datetime
from sqlmodel import SQLModel, Field


class PersonSkillHistory(SQLModel, table=True):
    personskill_id: int | None = Field(default=None, primary_key=True)
    date: datetime.date
    score: int
