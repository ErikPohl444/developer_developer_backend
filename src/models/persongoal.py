import datetime
from sqlmodel import SQLModel, Field


class PersonGoal(SQLModel, table=True):
    persongoal_id: int | None = Field(default=None, primary_key=True)
    goal_id: int = Field(foreign_key="goal.goal_id")
    person_id: int = Field(foreign_key="person.person_id")
    exceeds_score: int
    due_date: datetime.date
