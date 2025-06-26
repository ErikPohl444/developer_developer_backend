from sqlmodel import SQLModel, Field
import datetime


class PersonGoal(SQLModel, table=True):
    created_by: int = Field(foreign_key="user.user_id")
    create_date: datetime.datetime = Field(default = datetime.date.today)
    updated_by: int = Field(foreign_key="user.user_id")
    update_date: datetime.datetime = Field(default = datetime.date.today)
    persongoal_id: int | None = Field(default=None, primary_key=True)
    goal_id: int = Field(foreign_key="goal.goal_id")
    person_id: int = Field(foreign_key="person.person_id")
    exceeds_score: int
    due_date: datetime.date
