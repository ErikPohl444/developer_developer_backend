import datetime
from sqlmodel import SQLModel


class PersonGoal(SQLModel, table=True):
    goal_id: int
    person_id: int
    exceeds_score: int
    due_date: datetime.date
