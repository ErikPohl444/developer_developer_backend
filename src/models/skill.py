from sqlmodel import SQLModel


class Skill(SQLModel, table=True):
    skill_id: int
    name: str
