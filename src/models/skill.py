from sqlmodel import SQLModel


class Skill(SQLModel):
    skill_id: int
    name: str
