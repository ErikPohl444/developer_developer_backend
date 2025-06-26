from sqlmodel import SQLModel, Field


class PersonSkill(SQLModel, table=True):
    personskill_id: int | None = Field(default=None, primary_key=True)
    person_id: int
    skill_id: int
    score: int
