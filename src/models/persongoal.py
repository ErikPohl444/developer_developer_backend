import datetime
from sqlmodel import SQLModel

class PersonGoal(SQLModel):
    goal_id: int
    person_id: int
    exceeds_score: int
    due_date: datetime.date