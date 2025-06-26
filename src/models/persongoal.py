import datetime
from sqlmodel import SQLModel, Field


class PersonGoal(SQLModel, table=True):
    persongoal_id: int | None = Field(default=None, primary_key=True)
    goal_id: int
    person_id: int
    exceeds_score: int
    due_date: datetime.date
