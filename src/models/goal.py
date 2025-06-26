from sqlmodel import SQLModel, Field


class Goal(SQLModel, table=True):
    goal_id: int | None = Field(default=None, primary_key=True)
    skill_id: int
    name: str
