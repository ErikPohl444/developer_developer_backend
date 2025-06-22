from sqlmodel import SQLModel

class Goal(SQLModel):
    goal_id: int
    skill_id: int
    name: str