import datetime
from sqlmodel import SQLModel


class PersonSkillHistory(SQLModel):
    personskill_id: int
    date: datetime.date
    score: int