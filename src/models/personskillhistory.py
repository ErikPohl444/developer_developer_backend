import datetime
from sqlmodel import SQLModel


class PersonSkillHistory(SQLModel, table=True):
    personskill_id: int
    date: datetime.date
    score: int
