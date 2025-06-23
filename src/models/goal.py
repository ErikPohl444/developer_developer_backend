from sqlmodel import SQLModel


class Goal(SQLModel, table=True):
    goal_id: int
    skill_id: int
    name: str
