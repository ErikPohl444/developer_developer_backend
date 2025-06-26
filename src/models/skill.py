from sqlmodel import SQLModel, Field


class Skill(SQLModel, table=True):
    skill_id: int | None = Field(default=None, primary_key=True)
    name: str
